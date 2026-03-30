try:
    from langchain.agents import tool
    print('tool: langchain.agents')
except ImportError:
    try:
        from langchain_core.tools import tool
        print('tool: langchain_core.tools')
    except ImportError:
        print('tool: NOT FOUND')
try:
    from langchain.chat_models import ChatOpenAI
    print('ChatOpenAI: langchain.chat_models')
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
        print('ChatOpenAI: langchain_openai')
    except ImportError:
        print('ChatOpenAI: NOT FOUND')
try:
    from langchain.prompts import PromptTemplate
    print('PromptTemplate: langchain.prompts')
except ImportError:
    try:
        from langchain_core.prompts import PromptTemplate
        print('PromptTemplate: langchain_core.prompts')
    except ImportError:
        print('PromptTemplate: NOT FOUND')
try:
    from langchain.agents import initialize_agent, AgentType
    print('Agent: OK')
except ImportError:
    print('Agent: NOT FOUND')
