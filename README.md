# Charm Telemetry Template

This is a template repository for building custom Telemetry Exporters for the Charm ecosystem.
Use this to export metrics, traces, and LLM token usage to observability platforms like Datadog, LangSmith, or Sentry.

## How to build

1. Click **Use this template** on GitHub to create your own repository.
2. Rename the `src/charm_telemetry_helloworld` folder to your exporter's name (e.g. `src/charm_telemetry_datadog`).
3. Update `pyproject.toml` with your package name, dependencies, and `charm.telemetry` entry point.
4. Implement your hooks in `exporter.py` by inheriting from `BaseTelemetryExporter`.

## Publishing

```bash
uv build
uv publish
```

## Submitting to the Store

Once published to PyPI, submit a Pull Request to [here](https://github.com/charm-ai-labs/charm-community-plugin) to list your telemetry exporter in the official Charm Store!
