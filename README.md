# FileWatch

> Monitor local filesystem changes with a small, read-only tool.

FileWatch is a lightweight filesystem change monitor for development workflows, troubleshooting, and local integrity checks.

## Highlights

- Detect file changes during a watch session
- Read-only filesystem inspection
- Useful for development and debugging
- Simple terminal-oriented workflow
- Designed to stay lightweight

## Usage

```bash
filewatch ./project
filewatch ./project --interval 2
```

## Workflow

```text
filesystem
    ↓
snapshot
    ↓
change detection
    ↓
added / removed / modified
```

## Use Cases

- Watching generated files during development
- Diagnosing unexpected local changes
- Basic integrity monitoring
- Development tooling and automation

## Development

```bash
python -m unittest discover -s tests -v
```

## Safety

FileWatch reads filesystem metadata and content needed for comparison. It does not delete, modify, or execute files.

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
