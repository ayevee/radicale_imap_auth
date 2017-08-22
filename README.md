# Radicale Imap Authentication Plugin

Install the python module by running the following command in the same folder as `setup.py`:
```shell
python3 -m pip install --upgrade .
```

To make use this great creation in Radicale, set the configuration option type in the auth section to radicale_silly_auth:

```ini
[auth]
type = radicale_imap_auth
foo = bar
```

You can uninstall this module with:
```shell
python3 -m pip uninstall radicale_imap_auth
```
