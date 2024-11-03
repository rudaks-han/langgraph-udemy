from dotenv import load_dotenv

load_dotenv()

from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph

from nodes import execute_tools, run_agent_reasoning_engine
from state import AgentState

AGENT_REASON = "agent_reason"
ACT = "act"


def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT


flow = StateGraph(AgentState)

flow.add_node(AGENT_REASON, run_agent_reasoning_engine)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, execute_tools)


flow.add_conditional_edges(
    AGENT_REASON,
    should_continue,
)

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
# app.get_graph().draw_mermaid_png(
#     output_file_path="./graph.png",
#     draw_method=MermaidDrawMethod.PYPPETEER,
# )

if __name__ == "__main__":
    print("Hello, world!")
    res = app.invoke(
        # input={"input": "What is the weather in sf? Write it and the Triple it "}
        input={"input": "현재 서울 기온은 몇도야? 그리고 거기에 곱하기 3을 해줘"}
    )
    print(res)
