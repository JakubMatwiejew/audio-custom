# Static site served by nginx (Coolify: Build Pack = Dockerfile, port 80)
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html robots.txt sitemap.xml /usr/share/nginx/html/
COPY *.png *.jpg /usr/share/nginx/html/
EXPOSE 80
