
# Publishing this update safely

This ZIP is an **overlay**, not a replacement for the existing GitHub repository. It does not contain your earlier learning folders; keep those folders intact.

## Option A — GitHub website (manual upload)

1. Open https://github.com/jithin0joy/jithin0joy.github.io
2. Make a backup: Code → Download ZIP (or clone locally).
3. Add `index.html` and replace the root `README.md` with the supplied versions.
4. Upload the entire `Projects/graph-partitioning-gnn/` directory using Git or the GitHub web interface (which may require uploading files by directory).
5. Commit the changes on a new branch, inspect the diff, and merge after review.
6. In Settings → Pages, configure deployment from the main branch root if not already enabled.
7. Verify https://jithin0joy.github.io and the project link.

## Option B — Git commands (recommended)

```bash
git clone https://github.com/jithin0joy/jithin0joy.github.io.git
cd jithin0joy.github.io
git checkout -b portfolio-research-refresh
# Copy the contents of this ZIP into this directory; MERGE, do not delete old folders.
git add README.md index.html PUBLISHING.md Projects/graph-partitioning-gnn
git commit -m "Refresh portfolio and add MCA graph research reconstruction"
git push -u origin portfolio-research-refresh
```

Open a pull request on GitHub and review before merging. The repository URL and Pages URL are separate; a GitHub Pages website requires Pages settings and `index.html`.

## Safety checks

- Confirm both co-authors are correctly credited.
- Confirm any original student material is authorized for public release; none is included in this package.
- Do not commit client data, university IDs, email addresses of others, secrets or proprietary work artifacts.
- Run `pip install -r requirements.txt`, `python -m pytest -q`, and `python -m src.experiment --output results` inside the project directory.
- Do not describe the proposed GNN recommender as trained or deployed.

