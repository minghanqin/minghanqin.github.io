printf 'url: "http://127.0.0.1:4000"\n' > _config_local.yml
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 rbenv exec bundle exec jekyll serve --config _config.yml,_config_local.yml
