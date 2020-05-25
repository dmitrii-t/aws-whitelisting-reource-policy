FROM pulumi/pulumi:v2.2.1

ARG PULUMI_CONFIG_PASSPHRASE
ENV PULUMI_CONFIG_PASSPHRASE=${PULUMI_CONFIG_PASSPHRASE}

WORKDIR /workdir/app

COPY requirements.txt entrypoint.sh ./

RUN pip install -r requirements.txt \
    && addgroup --gid 1001 pulumi \
    && adduser --system --gid 1001 -uid 1001 pulumi \
    && mkdir /workdir/.pulumi \
    && chown -hR 1001:1001 /workdir

USER 1001

ENTRYPOINT ["./entrypoint.sh"]