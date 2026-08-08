FROM squidfunk/mkdocs-material:9 AS builder

WORKDIR /docs
COPY mkdocs.yml /docs/mkdocs.yml
COPY docs /docs/docs
RUN mkdocs build --strict

FROM nginx:alpine
COPY --from=builder /docs/site /usr/share/nginx/html
EXPOSE 80
