import os
import re
from mkdocs.utils import log

s3_base_url = "https://bucket-neu-2.s3.us-east-1.amazonaws.com"
asset_dirs = ['assets', 'images']

def on_page_markdown(markdown, page, config, files):
    """
    Replaces local asset paths with S3 URLs when in production build.
    """
    # Only run if MKDOCS_ENV is set to 'production' and S3_BASE_URL is provided
    # if os.environ.get('MKDOCS_ENV') != 'production' or not self.config['s3_base_url']:
    #     log.debug("LFS S3 Replacer: Not in production environment or S3_BASE_URL not set. Skipping URL replacement.")
    #     return markdown

    log.info(f"LFS S3 Replacer: Running in production. S3 Base URL: {s3_base_url}")

    # Regex to find Markdown image and link patterns: ![alt](path) and [text](path)
    # It captures the path inside the parentheses.
    # It looks for paths that start with one of the configured asset_dirs.
    # This assumes your Markdown links look like: ![img](../assets/my_image.png) or [file](../assets/my_file.zip)
    # This regex supports both relative `../assets/` and absolute `/assets/` linking for assets.
    
    # This pattern matches any relative path OR absolute path starting with asset_dirs
    # Example: (../assets/image.png) or (/assets/image.png)
    pattern = re.compile(r'(!?\[.*?\]\()(?P<path>(?:(?:(?:[a-zA-Z0-9_\-\.]+/?)+\/)?(?:' + '|'.join(re.escape(d) for d in asset_dirs) + r')(?:\/[^)]+)?))(\))')

    def replace_url(match):
        original_path = match.group('path') # The path captured by the regex
        # your links *in markdown* should be relative to the `docs` root, e.g., `/assets/image.png`
        # We will strip any leading slash to form the S3 key.
        s3_key_path = original_path.lstrip('/')
        s3_url = f"{s3_base_url}/{s3_key_path}"
        log.info(f"  Replacing {original_path} with {s3_url}")
        return f"{match.group(1)}{s3_url}{match.group(3)}"

    new_markdown = pattern.sub(replace_url, markdown)

    if new_markdown != markdown:
        log.info(f"LFS S3 Replacer: Replaced URLs on page {page.url}")
    else:
        log.debug(f"LFS S3 Replacer: No URLs replaced on page {page.url}")

    return new_markdown