FROM pulumi/pulumi:v2.2.1

ARG PULUMI_CONFIG_PASSPHRASE
ENV PULUMI_CONFIG_PASSPHRASE=${PULUMI_CONFIG_PASSPHRASE}

WORKDIR /.pulumi
WORKDIR /app

COPY requirements.txt entrypoint.sh ./

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]