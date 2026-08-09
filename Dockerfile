FROM python:3.12.10-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /project
COPY requirements-docs.txt ./requirements-docs.txt
RUN python -m pip install --no-cache-dir --requirement requirements-docs.txt

COPY mkdocs.yml ./mkdocs.yml
COPY docs ./docs
RUN python -m mkdocs build --strict --clean --site-dir /project/site

FROM nginx:1.27.4-alpine
COPY --from=builder /project/site /usr/share/nginx/html
EXPOSE 80
