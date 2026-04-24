# Odoo Development Guide for Agents

## Repository Overview
- Odoo is a web-based business application suite (ERP/CRM)
- Primary entrypoint: `odoo-bin` or `python3 -m odoo`
- Configuration via `odoo.tools.config` (command-line, config file, env vars)

## Key Commands
- Start server: `python3 odoo-bin -c config.conf` or `python3 odoo-bin --help` for options
- Run tests: `python3 odoo-bin -d database --test-enable --stop-after-init`
- Install addons: `python3 odoo-bin -d database -i module1,module2 --stop-after-init`
- Update addons: `python3 odoo-bin -d database -u module1,module2 --stop-after-init`

## Configuration
- Default config file: `~/.odoorc` (generated with `-s/--save`)
- Key options: `--addons-path`, `-d/--database`, `--db_user`, `--db_password`
- Environment variables: `ODOO_RC`, `PGDATABASE`, `PGUSER`, `PGPASSWORD`

## Testing
- Test cases: Inherit from `odoo.tests.common.TransactionCase`
- Run specific tests: `--test-tags :TestClass.test_method`
- Test file structure: `test_*.py` in `addons/*/tests/` directories

## Development Conventions
- Python 3.10+ required
- Code style: Ruff linting (see `ruff.toml`)
- Imports: Standard library, third-party, Odoo core, then local imports
- Addons structure: Each in `addons/` with `__manifest__.py` and `__init__.py`

## Common Pitfalls
- Never commit `--save` generated configs (contains sensitive data)
- Always use test cursors in test mode (registry test mode)
- Flush and invalidate caches appropriately in tests
- Use `odoo.tests.common.new_test_user()` for test user creation