def html_end_tag_by_start_tag(tag):
    return '</' + tag[1: tag.find(' ')] + '>'
