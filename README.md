# detection-old-iam

## Requirement

* python 3
* boto3

## OS ENVIRONMENT

Need to use `local`

```
#Example
$export CUSTOM_HOUR=****
$export ACCESS_ID=****
$export ACCESS_KEY=****
```

## How to use

### Local
```
#default hour is 1000
python3 detect-old-accesskeys.py

Or

hour = 1500
python3 detect-old-accesskeys.py ${hour}
```

### Docker

#### Docker Build
```
$cd source
$docker build . --build-arg ACCESS_ID=$ACCESS_ID --build-arg ACCESS_KEY=$ACCESS_KEY -t enaska0/detect-old-iam:latest
```

#### Docker Run
```
$docker run -v ${PWD}:/app enaska0/detect-old-iam:latest
```

#### Docker Push
```
$docker push enaska0/detect-old-iam:latest
```

