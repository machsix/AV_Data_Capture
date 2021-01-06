# AV Data Capture (CLI)

Forked from https://github.com/yoshiko2/AV_Data_Capture/wiki

It's heavily modified to support:
- run in alpine docker
- run the script at a different working directory
- sql database

## How to build?

### Local linux machine with stdlibc++

```bash
make
```

### Alpine with musl

```bash
sudo docker run --rm \
    -v "${PWD}:/src" \
    machsix/pyinstaller-alpine \
    --noconfirm \
    --onefile \
    --log-level DEBUG \
    --clean \
    AV_Data_Capture.spec
```