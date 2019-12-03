FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# RUN apt-get update


# -----------------------------------------

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
        ed \
        less \
        locales \
        vim-tiny \
        wget \
        icu-devtools \
        libiconv-hook-dev \
        libcurl4-gnutls-dev \
        ca-certificates \
        fonts-texgyre \
        libxml2-dev \
        build-essential \
        libcurl4-gnutls-dev \
        libxml2-dev \
        libssl-dev \
    && rm -rf /var/lib/apt/lists/*


RUN wget https://github.com/unicode-org/icu/releases/download/release-58-3/icu4c-58_3-src.tgz && tar -zxvf icu4c-58_3-src.tgz

WORKDIR icu/source 

RUN ./configure --prefix=/usr/local && make && make install

RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/icu/source/lib/

RUN wget https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz \
    && tar zxvf libiconv-1.16.tar.gz \
    && rm libiconv-1.16.tar.gz

WORKDIR libiconv-1.16

RUN ./configure --prefix=/usr/local && make && make install


## Configure default locale, see https://github.com/rocker-org/rocker/issues/19

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8

ENV LANG en_US.UTF-8

## Use Debian unstable via pinning -- new style via APT::Default-Release

RUN echo "deb http://http.debian.net/debian sid main" > /etc/apt/sources.list.d/debian-unstable.list \
        && echo 'APT::Default-Release "testing";' > /etc/apt/apt.conf.d/default

ENV R_BASE_VERSION 3.6.1

## Now install R and littler, and create a link for littler in /usr/local/bin

RUN apt-get update \
    && apt-get install -t unstable -y --no-install-recommends \
        littler \
                r-cran-littler \
        r-base=${R_BASE_VERSION}-* \
        r-base-dev=${R_BASE_VERSION}-* \
        r-recommended=${R_BASE_VERSION}-* \
    && ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
    && ln -s /usr/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
    && ln -s /usr/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
    && ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
    && install.r docopt \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm -rf /var/lib/apt/lists/*



COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module





WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
