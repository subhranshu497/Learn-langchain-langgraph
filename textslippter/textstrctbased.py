from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

text = """Investigators are digging deeper into the backgrounds of two terror suspects accused of tossing makeshift bombs at a protest outside the New York City mayor’s home in what authorities describe as an ISIS-inspired attack over the weekend.

Emir Balat, 18, and Ibrahim Kayumi, 19, both of Pennsylvania, are accused of trying to use improvised explosive devices at an anti-Islam demonstration and a counterprotest near Mayor Zohran Mamdani’s home Saturday. No device exploded."""

#initialize the splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size =100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)