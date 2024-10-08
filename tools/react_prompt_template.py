from langchain.prompts import PromptTemplate


def get_prompt_template():
    return PromptTemplate.from_template(
        """
            Answer the following questions as best you can. You have access to the following tools:

            {tools}

            Use the following format:

            Question: the input question you must answer

            Thought: you should always think about what to do, you can just answer if the question is something basic and not fact-based

            Action: the action to take, should be one of [{tool_names}]

            Action Input: the input to the action

            Observation: the result of the action

            ... (this Thought/Action/Action Input/Observation can repeat N times)

            Thought: I now know the final answer

            Final Answer: the final answer to the original input question

            Begin!

            Question: {input}

            Thought:{agent_scratchpad}
            """
    )
