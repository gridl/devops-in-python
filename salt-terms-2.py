Extract archive:
  archive.extracted:
    - name: /src/some-files
    - source: /src/some-files.tgz
    - archive_format: tar
  - require:
    - file: Copy archive
Copy archive:
  file.managed:
    - name: /src/some-files.tgz
    - source: salt://some-files.tgz