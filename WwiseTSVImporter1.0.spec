# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\02_Python\\WwiseTSVImporter\\WwiseTSVImporter1.0.py'],
             pathex=['D:\\02_Python'],
             binaries=[],
             datas=[('D:\\02_Python\\WwiseTSVImporter\\ncsound.ico', '.')],
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
          [],
          name='WwiseTSVImporter1.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False ,
          icon='D:\\02_Python\\WwiseTSVImporter\\ncsound.ico')