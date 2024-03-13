# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['app/main.py'],
             pathex=['app/main.py'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=True,
          name='vampire-survivors-profiler',
          debug=False,
          strip=False,
          upx=True,
          icon='icon.ico',
          console=False )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='dist/vampire-survivors-profiler')
