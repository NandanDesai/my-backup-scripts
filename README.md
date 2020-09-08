## My Backup Script

### On Linux PC

For the first time setup of backup system using rclone, refer the [rclone-guide.pdf](https://github.com/NandanDesai/my-backup-scripts/blob/master/rclone-guide.pdf) file. Once you have `rclone.conf` file generated, make sure to keep it somewhere safe. Use `rclone config file` command to know the location of `rclone.conf` file. You can use `rclone.conf` file to recover the backed up files on a new system.

**About the script:**

The backup script refers to `backup-paths` file to know what files/directories need to be backed up. It also refers to the same file to recover the files/directories when they're lost. Make sure that you keep `backup-paths` file safe as well along with `rclone.conf`.

**How to edit the `backup-paths` file:**

First write the name of the remote in square brackets and then followed by the backup paths.

The backup paths are separated by a colon. The LHS of the colon is the path on the local machine and the RHS of the colon is the path on the remote.

Example:

```
[google-drive-encrypted-linux]

/home/nandan/Desktop/TEST_BACKUP:test
/home/nandan/Desktop/test_backup_dir/:test
```

Also note that if you are backing up an entire directory on the local machine, then the path must end with '/' else it will be considered as a file and may cause inconsistency while recovering the data.

**How to use the script:**

The script can take only two commands: `backup` and `recover`. 

When you `backup`, it'll refer to the paths mentioned in the `backup-paths` file and copies the files/directories to the remote (the remote which is mentioned in backup-paths file). Already copied files will be skipped.

```bash
python3 backup.py backup
```

When you recover, it'll check if the files/directories mentioned in the `backup-paths` file exist or not. If they don't exist, then the file will be downloaded and placed in that exact location. If any file is missing in the backed up directory, then only that particular file is downloaded and placed instead of downloading the whole directory.

```bash
python3 backup.py recover
```

If you want to recover the entire backup to be downloaded into a particular directory:

```bash
python3 backup.py recover <path to custom dir>
```

Example:

```bash
python3 backup.py recover /home/nandan/Desktop/recovery_test
```


