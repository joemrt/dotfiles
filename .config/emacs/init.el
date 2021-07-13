(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["black" "#d55e00" "#009e73" "#f8ec59" "#0072b2" "#cc79a7" "#56b4e9" "white"])
 '(custom-enabled-themes '(dracula))
 '(custom-safe-themes
   '("549ccbd11c125a4e671a1e8d3609063a91228e918ffb269e57bd2cd2c0a6f1c6" default))
 '(display-line-numbers-type 'relative)
 '(package-selected-packages
   '(dracula-theme counsel org-bullets company-org-block company ivy vterm evil-leader evil-collection magit linum-relative auctex evil-commentary evil-surround use-package key-chord evil lua-mode ##)))
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
(org-babel-load-file "~/.config/emacs/config.org")
