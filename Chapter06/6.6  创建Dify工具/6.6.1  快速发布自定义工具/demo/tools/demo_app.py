#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 21:24
# @Author  : yongjie.su
# @File    : demo_app.py
# @Software: PyCharm
import requests
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage

from typing import Any, Dict, List, Union

# 可改成自己机器的IP地址
url = "http://127.0.0.1:5000/get/answer"


def _result(query, result_type, api_key=None):
    params = {
        "question": query,
        "secret": api_key
    }
    response = requests.get(url, params=params, timeout=60)
    # print(response)
    if response.status_code == 401 or 'error' in response.json():
        return response.json().get('error')
    # print(response.json())
    answer = response.json().get('answer')
    if result_type == 'string':
        answer = str(answer)
    return answer


class DemoAPPTool(BuiltinTool):
    def _invoke(self,
                user_id: str,
                tool_parameters: Dict[str, Any],
                ) -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
            invoke tools
        """
        query = tool_parameters['query']
        result_type = tool_parameters['result_type']
        api_key = self.runtime.credentials['demo_api_key']
        result = _result(query, result_type, api_key=api_key)

        return self.create_text_message(text=result)
