# Codex GitHub workflow sandbox

A disposable public repository for testing PR triage, failing checks, debugging, and review workflows with Codex.

## Security boundaries

- Contains sample data and dependency-free example code only.
- Never add secrets, credentials, personal data, production URLs, or proprietary code.
- GitHub Actions receives read-only repository contents permission.
- Third-party actions are pinned to immutable commit SHAs.
- CI uses `pull_request`, never `pull_request_target`, and does not expose secrets.
