from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

loader = PyPDFLoader('/Users/subh/Documents/interview/RESUME_SUBHRANSHUMOHAPATRA.pdf')
docs = loader.load() 

splitter = CharacterTextSplitter(
    chunk_size =100,
    chunk_overlap = 0,
    separator =''
)

res = splitter.split_documents(docs)

print(res)
print(res[0].page_content)
