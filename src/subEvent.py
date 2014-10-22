import lucene
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version, QueryParser, IndexSearcher
import sys
import simplejson
import os
import shutil

eventDict = {}
eventList = []
eventNum = 0

def index(string):
 lucene.initVM()
 indexDir = "REMOVEME.index-dir"
 dir = SimpleFSDirectory(File(indexDir))
 analyzer = StandardAnalyzer(Version.LUCENE_30)
 try:
  writer = IndexWriter(dir, analyzer, False, IndexWriter.MaxFieldLength(512))
 except lucene.JavaError:
  writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))
#e = sys.exc_info()[0]
#print e
#print >> sys.stderr, "Currently there are %d documents in the index..." % writer.numDocs()

 doc = Document()
 doc.add(Field("text", string, Field.Store.YES, Field.Index.ANALYZED))
 writer.addDocument(doc)
 #print 'In the index function'
 #print writer.numDocs()

#print >> sys.stderr, "Indexed lines from stdin (%d documents in index)" % (writer.numDocs())
#print >> sys.stderr, "About to optimize index of %d documents..." % writer.numDocs()
 writer.optimize()
#print >> sys.stderr, "...done optimizing index of %d documents" % writer.numDocs()
#print >> sys.stderr, "Closing index of %d documents..." % writer.numDocs()
 writer.close()


def retrieve(string,tweetID):
 global eventNum
 global eventDict
 global eventList
 lucene.initVM()
 indexDir = "REMOVEME.index-dir"
 dir = SimpleFSDirectory(File(indexDir))
 analyzer = StandardAnalyzer(Version.LUCENE_30)
 try:
  searcher = IndexSearcher(dir)
 except lucene.JavaError:
  #print 'Inside First Except'
#index(string)
  eventDict[tweetID] = eventNum
  eventNum = eventNum + 1
  return
#searcher = IndexSearcher(dir)
 try:
  query = QueryParser(Version.LUCENE_30, "text", analyzer).parse(string)
#e = sys.exc_info()[0]
#print e
  MAX = 2
  hits = searcher.search(query, MAX)
#print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)

  if hits.totalHits > 0:
#print hits.scoreDocs[0].doc
        #print hits.scoreDocs[0].doc
	#print tweetID
	print tweetID, hits.scoreDocs[0].doc
	eventDict[tweetID] = eventDict[hits.scoreDocs[0].doc]
  elif hits.totalHits == 0:
  	eventDict[tweetID] = eventNum
	eventNum = eventNum + 1

  for hit in hits.scoreDocs:
#print hit.score, hit.doc, hit.toString()
      doc = searcher.doc(hit.doc)
#print doc.get("text").encode("utf-8")
 except lucene.JavaError:
  pass

if __name__ == "__main__":
 global eventDict
 global eventList
 dirname = os.path.expanduser('~') + '/Projects/Sem2/IRE/IRE-Group13/REMOVEME.index-dir'
 try:
     shutil.rmtree(dirname)
 except OSError:
     pass
 
 with open("SNOW2014_Tweets.txt","r") as f:
  tweetID = 0
  for l in f:
   retrieve(l,tweetID)
   index(l)
   tweetID = tweetID + 1
 
 for i in range(eventNum):
	eventList.append([k for k, v in eventDict.iteritems() if v ==  i])
 
 f = open('output.txt', 'w')
 simplejson.dump(eventList, f)
 f.close()
