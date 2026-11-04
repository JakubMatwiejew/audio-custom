# Static site served by nginx (Coolify: Build Pack = Dockerfile, port 80)
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html site.css site.js robots.txt sitemap.xml /usr/share/nginx/html/
COPY *.png *.jpg /usr/share/nginx/html/
COPY space-echo-re-201-panel /usr/share/nginx/html/space-echo-re-201-panel
COPY chorus-echo-re-301-panel /usr/share/nginx/html/chorus-echo-re-301-panel
COPY makers /usr/share/nginx/html/makers
COPY parts /usr/share/nginx/html/parts
EXPOSE 80
