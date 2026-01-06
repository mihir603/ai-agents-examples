from autogen import ConversableAgent, UserProxyAgent, LLMConfig
config = LLMConfig.from_json(env="OAI_CONFIG_LIST")
assistant = ConversableAgent("agent-1", llm_config={"config_list" : config.config_list})

user_proxy = UserProxyAgent(
  "user",
  code_execution_config={
    "work_dir" : "working",
    "use_docker" : False
  },
  human_input_mode="ALWAYS",
  is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

user_proxy.initiate_chat(assistant, message="Write a Chess Game using Javascript, html and css?")