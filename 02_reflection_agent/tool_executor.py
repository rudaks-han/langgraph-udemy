from typing import List

from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage

from schemas import AnswerQuestion


def execute_tools(state: List[BaseMessage]) -> List[ToolMessage]:
    pass


if __name__ == "__main__":
    print("Tool Executor Enter")

    human_message = HumanMessage(
        content="Write about AI-Powered SOC / autonomous soc problem domain, "
        " list startups that do that and raised capital."
    )

    answer = AnswerQuestion
