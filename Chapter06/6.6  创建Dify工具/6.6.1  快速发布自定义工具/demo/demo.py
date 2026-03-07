#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 21:29
# @Author  : yongjie.su
# @File    : RAGAS中的Prompt.py
# @Software: PyCharm
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError

from core.tools.provider.builtin.demo.tools.demo_app import DemoAPPTool

from typing import Any, Dict


class DemoProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        try:
            DemoAPPTool().fork_tool_runtime(
                runtime={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_parameters={
                    "query": "test",
                    "result_type": "text"
                }
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
