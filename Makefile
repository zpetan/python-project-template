
GENERATE_MAINBRANCH = $(shell git remote show origin | sed -n '/HEAD branch/s/.*: //p')
SET_MAINBRANCH = $(eval MAINBRANCH=$(GENERATE_MAINBRANCH))

mainbranch:
	$(SET_MAINBRANCH)
	@echo $(MAINBRANCH)

check_remote:
	git fetch
	git branch -a

git_update:
	git pull origin $(shell git rev-parse --abbrev-ref HEAD) --rebase

git_synced:
	$(SET_MAINBRANCH)
	@echo $(MAINBRANCH)
	git pull origin $(MAINBRANCH) --rebase

git_squash:
	git rebase -v -i $(MAINBRANCH)
