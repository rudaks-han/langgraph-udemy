from typing import Any, Dict

from graphs.chains.retrieval_grader import retrieval_grader
from graphs.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = False
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score.binary_score
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            print(f"[doc] {d.page_content}")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            print(f"[doc] {d.page_content}")

    if len(filtered_docs) == 0:
        web_search = True

    print(f"len(filtered_docs) : {len(filtered_docs)}")
    return {"documents": filtered_docs, "question": question, "web_search": web_search}
