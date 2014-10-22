import lucene
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version, QueryParser, IndexSearcher
import sys

def index(string):
 lucene.initVM()
 indexDir = "REMOVEME.index-dir"
 dir = SimpleFSDirectory(File(indexDir))
 analyzer = StandardAnalyzer(Version.LUCENE_30)
 writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))

 print >> sys.stderr, "Currently there are %d documents in the index..." % writer.numDocs()

 doc = Document()
 doc.add(Field("text", string, Field.Store.YES, Field.Index.ANALYZED))
 writer.addDocument(doc)

 print >> sys.stderr, "Indexed lines from stdin (%d documents in index)" % (writer.numDocs())
 print >> sys.stderr, "About to optimize index of %d documents..." % writer.numDocs()
 writer.optimize()
 print >> sys.stderr, "...done optimizing index of %d documents" % writer.numDocs()
 print >> sys.stderr, "Closing index of %d documents..." % writer.numDocs()
 writer.close()
 
index("Hello World")
