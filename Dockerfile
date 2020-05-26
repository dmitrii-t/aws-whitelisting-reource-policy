FROM pulumi/pulumi:v2.2.1

ARG PULIMI_UID
ARG PULUMI_CONFIG_PASSPHRASE
ENV PULUMI_CONFIG_PASSPHRASE=${PULUMI_CONFIG_PASSPHRASE}

RUN addgroup --gid $PULIMI_UID pulumi \
    && adduser --system --gid $PULIMI_UID -uid $PULIMI_UID pulumi

WORKDIR /home/pulumi/app

COPY requirements.txt entrypoint.sh ./

RUN pip install -r requirements.txt

USER $PULIMI_UID

ENTRYPOINT ["./entrypoint.sh"]