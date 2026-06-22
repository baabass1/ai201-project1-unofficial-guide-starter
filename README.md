# Guide — Project 1

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

This project covers Python programming fundamentals. The knowledge base includes beginner-level topics such as variables, data types, lists, dictionaries, functions, loops, conditionals, file handling, error handling, and object-oriented programming.

This knowledge is valuable because many new programmers need quick and accurate explanations of Python concepts while learning to code. Although official Python documentation exists, it is often written as a technical reference rather than a beginner-friendly learning resource. Beginners frequently have to search through multiple tutorials, websites, and examples to understand a concept.

This system makes that information easier to access by providing grounded answers from a curated collection of Python learning documents. Instead of searching through multiple sources, users can ask a question in natural language and receive a concise response based on the available educational materials.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->


| #| Source                   | Type                 | URL or location                      |
| -| -------------------------| ---------------------| -------------------------------------|
| 1| python_variables.txt     | Local text document  | documents/python_variables.txt|
| 2| python_data_types.txt    | Local text document  | documents/python_data_types.txt      |
| 3| python_lists.txt         | Local text document  | documents/python_lists.txt           |
| 4| python_dictionaries.txt  | Local text document  | documents/python_dictionaries.txt    |
| 5| python_functions.txt     | Local text document  | documents/python_functions.txt       |
| 6| python_loops.txt         | Local text document  | documents/python_loops.txt           |
| 7| python_conditionals.txt  | Local text document  | documents/python_conditionals.txt    |
| 8| python_file_handling.txt | Local text document  | documents/python_file_handling.txt   |
| 9| python_error_handling.txt|Local text document   | documents/python_error_handling.txt  |
|10| python_oop.txt           | Local text document  | documents/python_oop.txt             |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** One complete document per chunk (approximately 450–750 characters)

**Overlap:** 0 characters

**Why these choices fit your documents:** The documents are short educational notes focused on individual Python topics. Since each file contains a complete explanation of a single concept, splitting documents into smaller chunks would separate related information and reduce retrieval quality.

**Final chunk count:** 10 chunks total, one chunk for each document.

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document     | Chunk text                                                                               |
|---|---------------------|------------------------------------------------------------------------------------------|
| 1 |python_variables.txt | Python Variables. Variables are used to store data in a Python program. A variable is created when a value is assigned to it.|
| 2 |python_data_types.txt| Python supports several built-in data types used to store different kinds of information. Common data types include String, Integer, Float, and Boolean. |
| 3 |python_functions.txt | Functions are reusable blocks of code that perform specific tasks. A function is defined using the def keyword and can accept parameters and return values. |
| 4 |python_dictionaries.txt| Dictionaries store data as key-value pairs. Each key is unique and is used to access its associated value. |
| 5 |python_oop.txt       | Object-oriented programming (OOP) organizes code using classes and objects. Classes act as blueprints, while objects are instances of classes. |

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 from Sentence Transformers.

**Production tradeoff reflection:** I selected all-MiniLM-L6-v2 because it is lightweight, fast, and performs well for semantic search on short educational documents. For a production system, I would evaluate larger embedding models that provide stronger multilingual support, better domain-specific understanding, and higher retrieval accuracy. The tradeoff would be increased cost, storage requirements, and inference latency.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:** What is a Python variable?

Top returned chunks:
- python_variables.txt
- python_data_types.txt
- python_functions.txt

Relevance explanation: The top result was python_variables.txt, which directly explains what a variable is, how variables are created, and how values are assigned. The data types document was also relevant because variables store values of different data types.

---

**Query 2:** What is a dictionary?

Top returned chunks:
- python_dictionaries.txt
- python_lists.txt
- python_variables.txt

Relevance explanation: The top result was python_dictionaries.txt, which directly explains key-value pairs and dictionary usage. The lists document was also relevant because both lists and dictionaries are commonly used Python data structures.

---

**Query 3:** What is object oriented programming?

Top returned chunks:
- python_oop.txt
- python_functions.txt
- python_variables.txt

Relevance explanation: The top result was python_oop.txt because it contains information about classes, objects, and object-oriented programming concepts. The functions and variables documents were retrieved because they contain related programming terminology, although they are less relevant than the OOP document.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** "Answer only using the provided context. If the answer is not in the context, say you do not know."
 
**How source attribution is surfaced in the response:** The system retrieves the top three relevant documents from ChromaDB and combines them into a context block that is sent to the language model. The model is instructed to answer only from this retrieved context and refuse questions that cannot be answered from the retrieved documents.

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1** 

Query: What is a Python variable?

Response: A Python variable is used to store data in a Python program and is created when a value is assigned to it.

Source attribution: python_variables.txt

---

**Grounded response 2**

Query: What is object oriented programming?

Response: Object-oriented programming (OOP) organizes code using classes and objects. Classes act as blueprints, while objects are instances of classes.

Source attribution: python_oop.txt

---

**Out-of-scope query**

Query: Who won the 2022 FIFA World Cup?

System response (refusal): I do not know.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:** A single text box labeled "Ask a Python Question" where users enter a Python-related question.

**Output format:** A text response generated by the Groq Llama 3.3 70B model using information retrieved from the document collection.

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

**User:** What is a Python variable?

**System:** A Python variable is used to store data in a Python program and is created when a value is assigned to it.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->


| # | Question                             | Expected answer           | System response (summarized)                                                         | Retrieval quality | Response accuracy |
| - | ------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------- | ----------------- |
| 1| What is a Python variable?           | A variable stores data and is created when a value is assigned.| Correctly explained                                                              | Relevant          | Accurate          |
| 2| What is a list?                      | A list is an ordered, mutable collection that can contain duplicate values. | Correctly described lists                                    | Relevant          | Accurate          |
| 3| What is a dictionary?                | A dictionary stores information as key-value pairs.            | Correctly explained dictionaries and key-value pair storage.                     | Relevant          | Accurate          |
| 4| What is object oriented programming? | OOP organizes code using classes and objects.                  | Correctly explained classes, objects, and the purpose of OOP.                    | Relevant          | Accurate          |
| 5| Who won the 2022 FIFA World Cup?     | The system should refuse because the answer is not in the documents. | Returned "I do not know."                                              | Relevant          | Accurate          |


**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** Who won the 2022 FIFA World Cup?

**What the system returned:** I do not know.

**Root cause (tied to a specific pipeline stage):** The document collection only contains Python programming documents. During the retrieval stage, ChromaDB could not retrieve any chunk containing information about the FIFA World Cup because no such information exists in the vector database. As a result, the language model did not receive relevant context and followed the grounding instruction to refuse the question.

**What you would change to fix it:** If the goal were to answer sports-related questions, I would expand the document collection to include sports documents and re-index them in ChromaDB. Alternatively, I could broaden the knowledge base by adding documents from multiple domains and improving retrieval filtering to better match user intent.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** The planning document helped me organize the project before writing code. Defining the document sources, retrieval approach, evaluation questions, and architecture made it easier to build each stage of the RAG pipeline step by step. It also provided clear testing criteria that I used to verify the system after implementation.

**One way your implementation diverged from the spec, and why:** My implementation used one chunk per document rather than splitting documents into smaller chunks. After reviewing the document collection, I found that each file was already short and focused on a single topic. Using entire documents as chunks simplified the pipeline and preserved context without negatively affecting retrieval quality.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* My project requirements, document structure, and retrieval goals for building a RAG system using Python documents.
- *What it produced:* Code for loading text files, generating embeddings with SentenceTransformer, storing vectors in ChromaDB, and retrieving relevant
- *What I changed or overrode:* I chose to use one chunk per document instead of implementing smaller chunk sizes because the documents were already short and focused on a single topic.

**Instance 2**

- *What I gave the AI:* My retrieval pipeline, Groq API requirements, and the requirement to build a user interface for querying the system.
- *What it produced:* Code that integrated the Groq API for grounded answer generation and a Gradio interface that allowed users to enter questions and receive responses.
- *What I changed or overrode:* I modified the generation step to include a grounding instruction that forces the model to answer only from retrieved context and return "I do not know" when the answer is not available in the documents.
