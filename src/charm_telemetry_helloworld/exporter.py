import os
import logging
from typing import Any, Dict
# pyrefly: ignore [missing-import]
from charm.core.telemetry import BaseTelemetryExporter

logger = logging.getLogger(__name__)

class HelloWorldExporter(BaseTelemetryExporter):
    """
    A minimal HelloWorld Telemetry Exporter for Charm.
    """
    def __init__(self) -> None:
        super().__init__()
        # Initialize your API clients here (e.g., Datadog, LangSmith)
        self.api_key = os.getenv("HELLOWORLD_API_KEY", "")

    def on_run_start(self, run_id: str, inputs: Dict[str, Any]) -> None:
        logger.info(f"[HelloWorldExporter] Run started: {run_id}")

    def on_run_end(self, run_id: str, outputs: Dict[str, Any]) -> None:
        logger.info(f"[HelloWorldExporter] Run ended: {run_id}")

    def on_error(self, run_id: str, error: Exception) -> None:
        pass

    def on_tool_start(self, tool_name: str, input_str: str) -> None:
        pass

    def on_tool_end(self, tool_name: str, output: str) -> None:
        pass

    def on_tool_error(self, tool_name: str, error: BaseException) -> None:
        pass

    def on_llm_new_token(self, token: str) -> None:
        # Example: count tokens or stream to external service
        pass

    def on_agent_action(self, tool: str, tool_input: str) -> None:
        pass
