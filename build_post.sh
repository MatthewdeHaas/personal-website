set -e

POST_MD=$1
POST_NAME=$(basename "$POST_MD" .md)

# Generate body only
pandoc -s "$POST_MD" -o "app/static/media/blogs/${POST_NAME}.html"

# Remove styling
sed -i '' '/max-width: 36em;/d' "app/static/media/blogs/${POST_NAME}.html"
