from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh import index
from whoosh import scoring
from whoosh.qparser import QueryParser

class IndexSearch:
    def __init__(self, dir_name):
        # Переменная схемы Индекса
        self.schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True), textdata=STORED)
        # Переменная папки, где будет создан Индекс
        self.dir_name = dir_name
        # Переменная экземпляра Индекса
        self.ind = index.create_in(dirname=dir_name, schema=self.schema)

    # Функция создания Индекса
    def create_index(self, content_text1, content_text2):
        writer = self.ind.writer()
        writer.add_document(title=u"doc1", content=f'u{content_text1}', path=u"/a", textdata=u"page 1")
        writer.add_document(title=u"doc2", content=f'u{content_text2}', path=u"/a", textdata=u"page 2")
        writer.commit()

    # Функция поиска в Индексе
    def search_index(self, search_text):
        with self.ind.searcher(weighting=scoring.Frequency) as searcher:
             query = QueryParser("content", self.ind.schema).parse(search_text)
             results = searcher.search(query, terms=True)
             for r in results:
                 print (r, r.score)
                 print(r['path'])
                 print(r['title'])
                 print(r['textdata'])
                 print(r.results)
                 print(r.docnum)
                 print(r.values())
                 print(r.items())
                 print(r.fields())
                 print(r.pos)
                 print(r.rank)
                 print(r.reader)
                 print(r.searcher)
                 if results.has_matched_terms():
                     print(results.matched_terms())
                     s = results.matched_terms()
                     for i, elem in enumerate(s):
                         print(elem[1].decode('utf-8'))
                     for hit in results:
                         print(hit.matched_terms())
