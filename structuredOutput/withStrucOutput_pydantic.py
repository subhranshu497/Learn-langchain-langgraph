from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-4-0613", temperature=0.7)

#create aschema
class ReviewSummary(BaseModel):
    key_themes: list[str] = Field(description="write down the key themes mentioned in the review in a list of strings")
    summary: str = Field(description="A concise summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="The overall sentiment of the review (positive, negative, or neutral)")
    pros: Optional[list[str]] = Field(default=None, description="List the pros mentioned in the review") 
    cons: Optional[list[str]] = Field(default=None, description="List the cons mentioned in the review") 
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer if mentioned in the review")

struct_model = model.with_structured_output(ReviewSummary)

result = struct_model.invoke("""After using the ZenBeam ultra-portable projector for the past three weeks, 
                      I am genuinely impressed by how much punch this little device packs into such a compact frame. 
                      The setup was incredibly intuitive, and within five minutes of unboxing, I was streaming a movie in 1080p directly onto my bedroom wall 
                      with surprisingly vibrant colors and deep contrast. While the built-in speakers are clear enough for a small room, I found that pairing it with 
                      a Bluetooth soundbar really completed the "home cinema" experience. My only minor gripe is that the cooling fan can get a bit audible during quiet 
                      scenes, and you definitely need a dark room to get the best out of the brightness levels. Overall, for anyone looking for a versatile projector 
                      that fits in a backpack and doesn't break the bank, this is an excellent choice that balances performance and portability perfectly.""")

print(result)


