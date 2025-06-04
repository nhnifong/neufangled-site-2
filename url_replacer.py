import os
import re
from mkdocs.utils import log

s3_base_url = "https://bucket-neu-2.s3.us-east-1.amazonaws.com/docs"
asset_dirs = ['assets', 'images']

def on_page_markdown(markdown, page, config, files):
    """
    Replaces local asset paths with S3 URLs when in production build.
    """
    # Only run if MKDOCS_ENV is set to 'github' and S3_BASE_URL is provided
    if os.environ.get('MKDOCS_ENV') != 'github' or not self.config['s3_base_url']:
        log.debug("URL Replacer: Not in production environment or S3_BASE_URL not set. Skipping URL replacement.")
        return markdown

    # Regex to find Markdown image and link patterns
    # ![](images/ag/image4.png){}
    pattern = re.compile(r"(!\[.*\]\()(?P<path>(?:assets|images).+)(\)\{.*\})")

    def replace_url(match):
        original_path = match.group('path') # The path captured by the regex
        # your links *in markdown* should be relative to the `docs` root, e.g., `/assets/image.png`
        # We will strip any leading slash to form the S3 key.
        s3_key_path = original_path.lstrip('/')
        s3_url = f"{s3_base_url}/{s3_key_path}"
        log.info(f"  Replacing {original_path} with {s3_url}")
        return f"{match.group(1)}{s3_url}{match.group(3)}"

    new_markdown = pattern.sub(replace_url, markdown)
    return new_markdown