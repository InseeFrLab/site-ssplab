FROM python:alpine
ENV SECRET_KEY=changeme
ENV DEBUG=False
ENV ALLOWED_HOSTS=*
WORKDIR /app
# Install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY site_ssplab/. .
COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]