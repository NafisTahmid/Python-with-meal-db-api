def list_html_list(any_list):
    start = '<!-- wp:list --><ul class="wp-block-list">'
    for element in any_list:
        start += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

def dict_list(dicts):
    start = '<!-- wp:list --><ul class="wp-block-list">'

    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong>:{value.title()}</li><!-- /wp:list-item -->'
    
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

def headers(username, password):
    import base64
    user = "NafisT"
    password = "Ng8U 58Zz ou08 VMNW 15Fd 0lu8"
    credential = f"{user}:{password}"
    token = base64.b64encode(credential.encode())
    code = {'Authorization': f'Basic {token.decode('utf-8')}'}
    return code

def image_url(source, name):
    start = '<!-- wp:image {"sizeSlug":"large"} -->'
    content = f'<figure class="wp-block-image size-large"><img src="{source}" alt="{name}"/>'
    end = '</figure><!-- /wp:image -->'
    code = f'{start}{content}{end}'
    return code


print(dict_list({'name':"Nafis", "age":"twenty six"}))