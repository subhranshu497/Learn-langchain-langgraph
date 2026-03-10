from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text ="""By 2026, the traditional 9-to-5 office model has largely evolved into what experts call the "Fluid Workforce." This paradigm prioritizes asynchronous collaboration and result-oriented environments over physical presence, enabled by sophisticated AI-driven project management tools. Professionals now navigate a "portfolio career," often contributing to multiple high-impact projects across different time zones simultaneously. This shift has empowered individuals to tailor their work around their personal lives, fostering a new era of work-life integration that was previously unimaginable.A flicker of light caught his eye—a transport shuttle making its slow, curved descent toward the inner ring. Down there, in the artificial gravity of the "Green Zone," millions lived in a perpetual twilight, unaware of the mechanical fragility that kept them breathing. Kaelen knew the structural integrity reports were failing; the ancient alloys were finally succumbing to the relentless radiation of the solar core. He turned away from the glass, the weight of a trillion lives resting on the encrypted drive tucked into his sleeve.
The late 18th century marked a radical departure from the agrarian life that had defined human existence for millennia, catalyzed by the perfection of the steam engine. As James Watt’s innovations moved from the coal mines to the textile mills, the very concept of time and labor was reimagined. Families moved from rural cottages to burgeoning urban centers, trading the seasonal rhythms of the farm for the relentless, clock-governed pace of the factory floor. This shift created unprecedented wealth but also exposed deep-seated social inequalities that would trigger a century of labor reform.Modern software architecture has shifted significantly toward microservices to handle the demands of global scalability. By decomposing a monolithic application into smaller, independent services, development teams can deploy updates to specific features without risking the entire system's stability. This modularity allows for "polyglot" environments where different services can be written in the most suitable language—such as a high-performance Java backend paired with a reactive Angular frontend—optimizing each component for its specific task."""

splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.5
)

#chunking
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)



