from langchain_community.graphs import Neo4jGraph
import getpass
import os
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
os.environ["NEO4J_URI"] = "neo4j://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = ""

graph = Neo4jGraph()

api_key = ""#输入API——key
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # 替换为实际的 API 地址
model = "qwen-plus"
llm = ChatOpenAI(model=model,api_key=api_key,base_url = base_url, temperature=0)

chain = GraphCypherQAChain.from_llm(graph=graph, llm=llm, verbose=True,allow_dangerous_requests=True)
response = chain.invoke({"query": "水肿应该吃什么中药，中药材的药性分别是什么"})
print(response)
