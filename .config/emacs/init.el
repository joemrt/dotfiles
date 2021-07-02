(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["black" "#d55e00" "#009e73" "#f8ec59" "#0072b2" "#cc79a7" "#56b4e9" "white"])
 '(custom-enabled-themes '(deeper-blue))
 '(package-selected-packages
   '(linum-relative auctex evil-commentary evil-surround use-package key-chord evil lua-mode ##)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Cantarell" :foundry "ABAT" :slant normal :weight normal :height 180 :width normal)))))

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
;; Comment/uncomment this line to enable MELPA Stable if desired.  See `package-archive-priorities`
;; and `package-pinned-packages`. Most users will not need or want to do this.
;;(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(package-initialize)


;; emulate vim behavior
;; evil mode
(setq evil-want-C-u-scroll t)
(require 'evil)
(evil-mode 1)
(evil-commentary-mode)

;; jk = Esc
(require 'key-chord)
(key-chord-mode 1)
(key-chord-define evil-insert-state-map  "jk" 'evil-normal-state)

;; logical line movement
(define-key evil-normal-state-map  (kbd "C-j")  'next-line)
(define-key evil-normal-state-map  (kbd "C-k")  'previous-line)


(defun get-my-init()
  "opens init.el in vertical split"
  (interactive)
  (split-window-horizontally)
 (find-file "~/.config/emacs/init.el")
  )

(key-chord-define evil-normal-state-map  "ev"  'get-my-init)


;; auctex options
(set-default 'preview-scale-function 1.2)

 (set-frame-parameter (selected-frame) 'alpha '(90  .   90))

;; relative line numbers
(require 'linum-relative)
(setq linum-relative-backend 'display-line-numbers-mode)
(linum-relative-global-mode)


;; org mode
(setq-default org-confirm-babel-evaluate nil)


;; buffer in same window
(global-set-key "\C-x\C-b" 'buffer-menu)
