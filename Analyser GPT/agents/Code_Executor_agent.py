# https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.CodeExecutorAgent

from autogen_agentchat.agents import CodeExecutorAgent
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor


def getCodeExecutorAgent(code_executor):

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutor',
        code_executor = code_executor
    )

    return code_executor_agent



    