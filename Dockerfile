FROM pulumi/pulumi:v2.2.1

ARG PULUMI_CONFIG_PASSPHRASE
ENV PULUMI_CONFIG_PASSPHRASE=${PULUMI_CONFIG_PASSPHRASE}

RUN addgroup --gid 1001 pulumi \
    && adduser --system --gid 1001 -uid 1001 pulumi

WORKDIR /home/pulumi/app

COPY requirements.txt entrypoint.sh ./

RUN pip install -r requirements.txt

USER 1001

#RUN pulumi login file://~ \
#    && pulumi plugin install resource aws v2.5.0

ENTRYPOINT ["./entrypoint.sh"]