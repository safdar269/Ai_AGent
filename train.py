<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1Hv0koyvHCNd91Vr1bZDS3DqGwHbXr87j -->
<html lang="en" theme="light" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="safdarshar6@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./train_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-KmhOiTn6sHD8dy14OaGi/9+f17owL+KWDoLiUoEjdbwL0MkY5QTE9wPi90EHLAnV" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./train_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-KmhOiTn6sHD8dy14OaGi/9+f17owL+KWDoLiUoEjdbwL0MkY5QTE9wPi90EHLAnV" nonce=""></script><script type="text/javascript" async="" src="./train_files/js" nonce=""></script><script src="./train_files/cb=gapi.loaded_0" nonce="" async=""></script><script nonce="">window.performance.mark('head_start');</script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>train.py - Colab</title><link href="./train_files/css2" rel="stylesheet"><link href="./train_files/css" rel="stylesheet"><script nonce="">
      window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    </script><script async="" src="./train_files/analytics.js.download" nonce=""></script><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_Jb{font:13px/27px Roboto,Arial,sans-serif;z-index:986}.gb_0{display:none}.gb_X{background-size:32px 32px;border:0;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_tb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_tb.gb_X{height:30px;width:30px}.gb_tb.gb_X:active,.gb_tb.gb_X:hover{box-shadow:none}.gb_ub{background:#fff;border:none;border-radius:50%;bottom:2px;box-shadow:0px 1px 2px 0px rgba(60,64,67,0.3),0px 1px 3px 1px rgba(60,64,67,0.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_vb{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25),(min-resolution:1.25dppx){.gb_X:before,.gb_wb:before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_ba .gb_wb:before{-webkit-transform:scale(scale(.416666667));transform:scale(scale(.416666667))}}.gb_X:focus,.gb_X:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_X:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_X:active:after{background:rgba(0,0,0,.1);border-radius:50%;content:"";display:block;height:100%}.gb_xb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_C.gb_xb{width:auto}.gb_xb:focus,.gb_xb:hover{opacity:.85}.gb_yb .gb_xb,.gb_yb .gb_zb{line-height:26px}#gb#gb.gb_yb a.gb_xb,.gb_yb .gb_zb{font-size:11px;height:auto}.gb_Ab{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_9a:hover .gb_Ab{opacity:.85}.gb_7a>.gb_z{padding:3px 3px 3px 4px}.gb_Bb.gb_sb{color:#fff}.gb_9 .gb_Ab,.gb_9 .gb_xb{opacity:1}#gb#gb .gb_9.gb_9 a.gb_xb,#gb#gb.gb_9.gb_9 a.gb_xb{color:#fff}.gb_9.gb_9 .gb_Ab{border-top-color:#fff;opacity:1}.gb_9 .gb_X:focus,.gb_9 .gb_X:hover,.gb_sa .gb_X:focus,.gb_sa .gb_X:hover{box-shadow:0 1px 0 rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.2)}.gb_Cb .gb_z,.gb_Db .gb_z{position:absolute;right:1px}.gb_9a.gb_8,.gb_Eb.gb_8,.gb_z.gb_8{-webkit-box-flex:0;-webkit-flex:0 1 auto;flex:0 1 auto}.gb_Fb.gb_Hb .gb_xb{width:30px!important}.gb_V,.gb_W{position:absolute}.gb_W{height:40px;right:-5px;top:-5px;width:40px}@-webkit-keyframes apd-ring-fade-in{0%{opacity:0}to{opacity:1}}@keyframes apd-ring-fade-in{0%{opacity:0}to{opacity:1}}.gb_V{height:42px;width:42px;-webkit-animation:apd-ring-fade-in .25s ease-in;animation:apd-ring-fade-in .25s ease-in}.gb_Ib .gb_W,.gb_Jb .gb_W{right:0;top:0}.gb_Ib .gb_V,.gb_Jb .gb_V,.gb_y .gb_V{right:-1px;top:-1px}.gb_y .gb_W{right:1px;top:-1px}.gb_Ra a.gb_4a{border-radius:100px;background:#0b57d0;background:var(--gm3-sys-color-primary,#0b57d0);box-sizing:border-box;color:#fff;color:var(--gm3-sys-color-on-primary,#fff);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_Ra a.gb_6a{border-radius:100px;border:1px solid;border-color:#747775;border-color:var(--gm3-sys-color-outline,#747775);background:none;box-sizing:border-box;color:#0b57d0;color:var(--gm3-sys-color-primary,#0b57d0);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_ab.gb_K a.gb_4a,.gb_bb.gb_K a.gb_4a,.gb_cb.gb_K a.gb_4a{background:#c2e7ff;background:var(--gm3-sys-color-secondary-fixed,#c2e7ff);color:#001d35;color:var(--gm3-sys-color-on-secondary-fixed,#001d35)}.gb_Ra.gb_K a.gb_6a{color:#a8c7fa;color:var(--gm3-sys-color-primary,#a8c7fa)}.gb_Ra a.gb_Xd{padding:10px 12px;margin:12px 16px 12px 10px;min-width:85px}@media (max-width:640px){.gb_Ra a.gb_Xd{min-width:75px}}.gb_Nd,.gb_Ra{font-family:Google Sans Text,Roboto,Helvetica,Arial,sans-serif;font-style:normal}.gb_Ra.gb_ab{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_ab.gb_Zd{background:#fff;background:var(--og-bar-background,var(--gm3-sys-color-background,#fff))}.gb_Ra.gb_ab .gb_yd.gb_zd,.gb_Ra.gb_ab a.gb_6,.gb_Ra.gb_ab span.gb_6{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_ab .gb_Ad .gb_0d,.gb_Ra.gb_ab .gb_rd .gb_0d{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_ab svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}@media (forced-colors:active) and (prefers-color-scheme:dark){.gb_Ra svg,.gb_Ra.gb_K svg,.gb_Ra.gb_ab svg{color:white}}.gb_Ra.gb_K.gb_ab{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_ab.gb_Zd{background:transparent}.gb_Ra.gb_K.gb_ab .gb_yd.gb_zd,.gb_Ra.gb_K.gb_ab a.gb_6,.gb_Ra.gb_K.gb_ab span.gb_6{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_ab .gb_Ad .gb_0d,.gb_Ra.gb_K.gb_ab .gb_rd .gb_0d{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_ab svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ra.gb_K.gb_ab.gb_Zd{background:#1f1f1f;background:var(--og-bar-background,var(--gm3-sys-color-background,#131314))}.gb_Ra.gb_bb{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_bb.gb_Zd{background:#e9eef6;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#e9eef6))}.gb_Ra.gb_bb .gb_yd.gb_zd,.gb_Ra.gb_bb a.gb_6,.gb_Ra.gb_bb span.gb_6{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_bb .gb_Ad .gb_0d,.gb_Ra.gb_bb .gb_rd .gb_0d{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_bb svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ra.gb_K.gb_bb{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_bb.gb_Zd{background:#282a2c;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#282a2c))}.gb_Ra.gb_K.gb_bb .gb_yd.gb_zd,.gb_Ra.gb_K.gb_bb a.gb_6,.gb_Ra.gb_K.gb_bb span.gb_6{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_bb .gb_Ad .gb_0d,.gb_Ra.gb_K.gb_bb .gb_rd .gb_0d{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ra.gb_K.gb_bb svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ra.gb_cb{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_cb.gb_Zd{background:transparent}.gb_Ra.gb_cb .gb_yd.gb_zd,.gb_Ra.gb_cb a.gb_6,.gb_Ra.gb_cb span.gb_6{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_cb .gb_Ad .gb_0d,.gb_Ra.gb_cb .gb_rd .gb_0d{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ra.gb_cb svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ra.gb_cb.gb_K.gb_Zd{background:transparent}.gb_Ra.gb_cb.gb_K .gb_yd.gb_zd,.gb_Ra.gb_cb.gb_K a.gb_6,.gb_Ra.gb_cb.gb_K span.gb_6{color:white;color:var(--og-theme-color,white)}.gb_Ra.gb_cb.gb_K .gb_Ad .gb_0d,.gb_Ra.gb_cb.gb_K .gb_rd .gb_0d{color:white;color:var(--og-theme-color,white)}.gb_Ra.gb_cb.gb_K svg{color:white;color:var(--og-theme-color,white)}.gb_Ra a.gb_6,.gb_Ra span.gb_6{text-decoration:none}.gb_yd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-box-flex:1;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_Dd{display:none}.gb_Ra.gb_ib .gb_yd{margin-bottom:0}.gb_Ad.gb_Bd .gb_yd{padding-left:4px}.gb_Ra.gb_ib .gb_Cd{position:relative;top:-2px}.gb_Ra{min-width:160px;position:relative}.gb_Ra.gb_jd{min-width:120px}.gb_Ra.gb_1d .gb_2d{display:none}.gb_Ra.gb_1d .gb_Td{height:56px}header.gb_Ra{display:block}.gb_Ra svg{fill:currentColor}.gb_3d{position:fixed;top:0;width:100%}.gb_4d{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_5d{height:64px}.gb_Td{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ra:not(.gb_ib) .gb_Td{padding:8px}.gb_Ra:not(.gb_ib) .gb_Td a.gb_6d{margin:12px 8px 12px 10px}.gb_Ra.gb_7d .gb_Td{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ra .gb_Td.gb_Ud.gb_8d{min-width:0}.gb_Ra.gb_ib .gb_Td{padding:4px;padding-left:8px;min-width:0}.gb_Ra.gb_ib .gb_Td a.gb_6d{margin:12px 8px 12px 10px}.gb_2d{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_9d>.gb_2d{display:table-cell;width:100%}.gb_Ad{padding-right:25px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ra.gb_ib .gb_Ad{padding-right:14px}.gb_ae{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_ae>:only-child{display:inline-block}.gb_be.gb_sd{padding-left:4px}.gb_Ra.gb_7d .gb_be,.gb_Ra.gb_ib:not(.gb_Nd) .gb_be,.gb_be.gb_ce{padding-left:0}.gb_Ra.gb_ib .gb_be.gb_ce{padding-right:0}.gb_Ra.gb_ib .gb_be.gb_ce .gb_7a{margin-left:10px}.gb_sd{display:inline}.gb_Ra.gb_Nd .gb_be.gb_de,.gb_Ra.gb_md .gb_be.gb_de{padding-left:2px}.gb_yd{display:inline-block}.gb_be{box-sizing:border-box;height:48px;padding:0 4px;padding-left:5px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Nd{height:48px}.gb_Ra.gb_Nd{min-width:auto}.gb_Nd .gb_be{float:right;padding-left:32px;padding-left:var(--og-bar-parts-side-padding,32px)}.gb_Nd .gb_be.gb_ee{padding-left:0}.gb_fe{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_a a,.gb_fd a{color:inherit}.gb_zd{text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_zd{opacity:1}.gb_ge{position:relative}.gb_R{font-family:arial,sans-serif;line-height:normal;padding-right:15px}.gb_7{display:inline-block;padding-left:15px}.gb_7 .gb_6{display:inline-block;line-height:24px;vertical-align:middle}.gb_he{text-align:left}.gb_O,.gb_P{display:none}@media screen and (max-width:319px){.gb_Td .gb_L{display:none;visibility:hidden}}.gb_L .gb_C,.gb_L .gb_C:focus,.gb_L .gb_C:hover{opacity:1}.gb_Q{display:none}.gb_1{display:none!important}.gb_sb{visibility:hidden}@media screen and (max-width:319px){.gb_Td:not(.gb_Ud) .gb_L{display:none;visibility:hidden}}.gb_Ed{display:inline-block;vertical-align:middle}.gb_Fd .gb_0{bottom:-3px;right:-5px}@if (RTL_LANG){.gb_Fd .gb_0{left:-5px}}.gb_Ed:first-child{padding-left:0}.gb_D{position:relative}.gb_C{display:inline-block;outline:none;vertical-align:middle;border-radius:50%;box-sizing:border-box;height:40px;width:40px}#gb#gb a.gb_C,.gb_C{cursor:pointer;text-decoration:none}.gb_C,a.gb_C{color:#000}x:-o-prefocus{border-bottom-color:#ccc}.gb_ta{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:0;top:54px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text;user-select:text}.gb_Ed.gb_eb .gb_ta,.gb_eb.gb_ta{display:block}.gb_Kd{position:absolute;right:0;top:54px;z-index:-1}.gb_yb .gb_ta{margin-top:-10px}.gb_Ed:first-child{padding-left:4px}.gb_Ra.gb_Ld .gb_Ed:first-child{padding-left:0}.gb_Md{position:relative}.gb_Nd .gb_Md,.gb_rd .gb_Md{float:right}.gb_C{padding:8px;cursor:pointer}.gb_C,.gb_Pd button svg{border-radius:50%}.gb_Ed{padding:4px}.gb_Ra.gb_Ld .gb_Ed{padding:4px 2px}.gb_Ra.gb_Ld .gb_z.gb_Ed{padding-left:6px}.gb_ta{z-index:991;line-height:normal}.gb_ta.gb_Rd{left:0;right:auto}@media (max-width:350px){.gb_ta.gb_Rd{left:0}}.gb_Sd .gb_ta{top:56px}.gb_z .gb_C{padding:4px}.gb_Z{display:none}.gb_9a:not(.gb_6d){position:relative}.gb_ke:after{content:"";border:1px solid #202124;opacity:.13;position:absolute;top:4px;left:4px;border-radius:50%;width:30px;height:30px;box-sizing:content-box}.gb_7a{box-sizing:border-box;cursor:pointer;display:inline-block;height:48px;overflow:hidden;outline:none;padding:7px 0 0 16px;vertical-align:middle;width:142px;border-radius:28px;background-color:transparent;border:1px solid;position:relative}.gb_7a .gb_9a{width:32px;height:32px;padding:0}.gb_7a .gb_V{top:2px;right:4px}.gb_7a .gb_0{bottom:-2px;right:-4px}.gb_ab .gb_7a,.gb_bb .gb_7a{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_ab.gb_K .gb_7a,.gb_bb.gb_K .gb_7a{border-color:#8e918f;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#8e918f))}.gb_cb .gb_7a{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_cb.gb_K .gb_7a{border-color:#e3e3e3;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_db{display:inherit}.gb_7a .gb_db{background:#fff;border-radius:6px;display:inline-block;left:15px;position:static;padding:2px;top:-1px;height:32px;box-sizing:border-box;width:78px}.gb_fb{text-align:center}.gb_fb.gb_gb{background-color:#f1f3f4}.gb_fb .gb_hb{vertical-align:middle;max-height:28px;max-width:74px}.gb_Ra .gb_7a .gb_z.gb_Ed{padding:0;margin-right:9px;float:right}.gb_Ra:not(.gb_ib) .gb_7a{margin-left:10px;margin-right:4px}.gb_7a .gb_ke:after{left:0;top:0}@media screen and (max-width:480px){.gb_7a .gb_db{display:none}.gb_7a{border:none;border-radius:50%;height:40px;margin:4px;outline:1px solid transparent;padding:0;width:40px}.gb_Ra .gb_7a .gb_z.gb_Ed{padding:4px;margin-right:0}}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.GWpPdFKEL-s.2019.O","com.pk","en","425",0,[4,2,"","","","973598045","0"],null,"hOabas3yBdn4mLQP2Y7DaA",null,0,"og.qtm.Slf9k6xbtbQ.L.W.O","AA2YrTuJWwymoLzabh5d8DnMJYz1k9It3Q","AA2YrTvWGogfe9gNdtCZFN4PB5nWDEkvlA","",2,1,200,"PAK",null,null,"425","425",1,null,null,114591953,null,0,0,1,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","safdarshar6@gmail.com","","AMvpoZufH4ufOX8ELElXkhgP7rWFO5FZ0glQTm9DC24egW-7uKB0dvvnbNfM0MyPwm1s9Wgwxrzct-Fq5gLeF0kdJnkWrKVqAQ",0,0,null,"",1,"Safdar Shar","https://lh3.googleusercontent.com/ogw/AF2bZygIo8mWzsdK8hNa_4_rG1KXT_GAIrOAqfalgm1-miDSbYWu=s83-c-mo"],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/notebook?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,null,[0.009999999776482582,"com.pk","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"PAK","en","973598045.0",8,null,1,0,null,null,null,null,"3700942,105140909,105140912,115517798,115517801,116690943,116690949,119852746,119852748,120281895,120281898",null,null,null,"hOabas3yBdn4mLQP2Y7DaA",0,0,0,null,2,5,"ie",60,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.GWpPdFKEL-s.2019.O/rt=j/m=qabr,q_dnp,qcwid,qapid,qads,qrcd/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTuJWwymoLzabh5d8DnMJYz1k9It3Q"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.Slf9k6xbtbQ.L.W.O/m=qcwid,qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTvWGogfe9gNdtCZFN4PB5nWDEkvlA"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026oame=1\u0026ame=1\u0026ube=1\u0026pppea=2\u0026dpi=114591953"],0,414,424,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/notebook\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,null,0,1,"Account alert",0],null,1,null,1,null,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,"(opens a new tab)",0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,0,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/notebook?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/notebook\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/notebook\u0026timeStmp=1788601988\u0026secTok=.AG5fkS98d2-k8rw4TrwoLDR-mgxAXyOGYQ\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,null,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fnotebook\u0026ec=GAZAqQM",null,null,0,null,null,null,0,null,null,null,0],null,0,0,[null,"https://colab.research.google.com/notebook",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",null,0,0,"","",null,0,null,86400,null,null,null,null,0,null,0,0,"1184720131",3,1,0,0,1],0,null,null,null,null,0,"safdarshar6@gmail.com",0,1,0,0,"Google membership",0,"CAMSAA==","1",0,"Close","Loading"],null,null,[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,0]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ia,oa,pa,ta,va,wa,Ia,Ja,ab,db,fb,kb,gb,mb,sb,Eb,Fb,Gb,Hb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{let c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.So=!0;return a};
_.ha=function(a){var b=a;if((0,_.ca)(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(da(b)&&!Number.isSafeInteger(b))throw Error(String(b));return ea?BigInt(a):a=fa(a)?a?"1":"0":(0,_.ca)(a)?a.trim()||"0":String(a)};ia=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){let d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ja=function(a){_.t.setTimeout(()=>{throw a;},0)};
_.la=function(){return _.ka().toLowerCase().indexOf("webkit")!=-1};_.ka=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};oa=function(a){if(!ma||!na)return!1;for(let b=0;b<na.brands.length;b++){let {brand:c}=na.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};_.u=function(a){return _.ka().indexOf(a)!=-1};pa=function(){return ma?!!na&&na.brands.length>0:!1};_.qa=function(){return pa()?!1:_.u("Opera")};_.ra=function(){return pa()?!1:_.u("Trident")||_.u("MSIE")};
_.sa=function(){return _.u("Firefox")||_.u("FxiOS")};_.ua=function(){return _.u("Safari")&&!(ta()||(pa()?0:_.u("Coast"))||_.qa()||(pa()?0:_.u("Edge"))||(pa()?oa("Microsoft Edge"):_.u("Edg/"))||(pa()?oa("Opera"):_.u("OPR"))||_.sa()||_.u("Silk")||_.u("Android"))};ta=function(){return pa()?oa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(pa()?0:_.u("Edge"))||_.u("Silk")};va=function(){return ma?!!na&&!!na.platform:!1};wa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};
_.xa=function(){return wa()||_.u("iPad")||_.u("iPod")};_.ya=function(){return va()?na.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};_.Fa=function(a){return a[Da]===Ea};_.Ha=function(a,b){return b===void 0?a.v!==Ga&&!!(2&(a.ma[_.v]|0)):!!(2&b)&&a.v!==Ga};Ia=function(a){return a};
Ja=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ka=function(a){a=Error(a);Ja(a,"warning");return a};_.Ma=function(a,b){if(a!=null){var c;var d=(c=La)!=null?c:La={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ja(a,"incident"),_.ja(a))}};_.Oa=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Na(a)+"`"+a);return a};_.Pa=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};
_.Ra=function(a){if(!(0,_.Qa)(a))throw _.Ka("enum");return a|0};_.Sa=function(a){return a==null?a:(0,_.Qa)(a)?a|0:void 0};_.Ta=function(a){if(typeof a!=="number")throw _.Ka("int32");if(!(0,_.Qa)(a))throw _.Ka("int32");return a|0};_.Ua=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Va=function(a){return a==null||typeof a==="string"?a:void 0};_.Wa=function(a,b,c){if(a!=null&&_.Fa(a))return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};
_.Za=function(a){var b=_.Xa(_.Ya);return b?a[b]:void 0};ab=function(a,b){b<100||_.Ma($a,1)};
db=function(a,b,c,d){var e=d!==void 0;d=!!d;var f=_.Xa(_.Ya),g;!e&&f&&(g=a[f])&&g.Rd(ab);f=[];var h=a.length;g=4294967295;var k=!1,l=!!(b&64),n=l?b&128?0:-1:void 0;if(!(b&1)){var p=h&&a[h-1];p!=null&&typeof p==="object"&&p.constructor===Object?(h--,g=h):p=void 0;if(l&&!(b&128)&&!e){k=!0;var q;g=((q=bb)!=null?q:Ia)(g-n,n,a,p,void 0)+n}}b=void 0;for(q=0;q<h;q++){let w=a[q];if(w!=null&&(w=c(w,d))!=null)if(l&&q>=g){let D=q-n;var r=void 0;((r=b)!=null?r:b={})[D]=w}else f[q]=w}if(p)for(let w in p){r=p[w];
if(r==null||(r=c(r,d))==null)continue;h=+w;let D;if(l&&!Number.isNaN(h)&&(D=h+n)<g)f[D]=r;else{let E;((E=b)!=null?E:b={})[w]=r}}b&&(k?f.push(b):f[g]=b);e&&_.Xa(_.Ya)&&(a=_.Za(a))&&"function"==typeof _.cb&&a instanceof _.cb&&(f[_.Ya]=a.j());return f};
fb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.eb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){let b=a[_.v]|0;return a.length===0&&b&1?void 0:db(a,b,fb)}if(a!=null&&_.Fa(a))return gb(a);if("function"==typeof _.hb&&a instanceof _.hb)return a.v();return}return a};kb=function(a,b){if(b){bb=b==null||b===Ia||b[ib]!==jb?Ia:b;try{return gb(a)}finally{bb=void 0}}return gb(a)};
gb=function(a){a=a.ma;return db(a,a[_.v]|0,fb)};
_.nb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(lb&&1&e)throw Error("m");2048&e&&!(2&e)&&mb();if(e&256)throw Error("n");if(e&64)return(e|d)!==e&&(a[_.v]=e|d),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;let k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<g)c[f+b]=
k[h],delete k[h];else break;e=e&-16760833|(g&1023)<<14;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-16760833|(h&1023)<<14}}}a[_.v]=e|64|d;return a};mb=function(){if(lb)throw Error("p");_.Ma(ob,5)};
sb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.pb(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&_.Fa(a))return b=a.ma,c=b[_.v]|0,_.Ha(a,c)?a:_.qb(a,b,c)?_.rb(a,b):_.pb(b,c);if("function"==typeof _.hb&&a instanceof _.hb)return a};_.rb=function(a,b,c){a=new a.constructor(b);c&&(a.v=Ga);a.A=Ga;return a};
_.pb=function(a,b,c,d){d!=null||(d=!!(34&b));a=db(a,b,sb,d);d=32;c&&(d|=2);b=b&16769217|d;a[_.v]=b;return a};_.tb=function(a){var b=a.ma,c=b[_.v]|0;return _.Ha(a,c)?_.qb(a,b,c)?_.rb(a,b,!0):new a.constructor(_.pb(b,c,!1)):a};_.ub=function(a){if(a.v!==Ga)return!1;var b=a.ma;b=_.pb(b,b[_.v]|0);b[_.v]|=2048;a.ma=b;a.v=void 0;a.A=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Ha(a,a.ma[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.qb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.v=Ga,!0):!1};_.xb=function(a,b,c,d,e){var f=c+(e?0:-1),g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){let h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>14&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.zb=function(a,b,c,d,e){var f=!1;d=_.yb(a,d,e,g=>{var h=_.Wa(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ha(d)&&_.wb(a,b),d};_.Ab=function(){var a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(){this.wa=this.wa;this.ha=this.ha};_.Bb=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Cb=function(a,b,c){for(let d in a)b.call(c,a[d],d,a)};_.Db=function(a){for(let b in a)return!1;return!0};
Eb=Object.defineProperty;Fb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Gb=Fb(this);Hb=function(a,b){if(b)a:{var c=Gb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Eb(c,a,{configurable:!0,writable:!0,value:b})}};
Hb("globalThis",function(a){return a||Gb});Hb("Symbol.dispose",function(a){return a?a:Symbol("b")});var Kb,Lb,Ob;_.Ib=_.Ib||{};_.t=this||self;Kb=function(a,b){var c=_.Jb("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Lb=_.t._F_toggles_gbar_||[];_.Jb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Na=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Mb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Nb="closure_uid_"+(Math.random()*1E9>>>0);
Ob=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Ob;return _.z.apply(null,arguments)};_.Pb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Xa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.da=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.base=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Qb=!!(Lb[0]>>24&1),Rb=!!(Lb[0]>>19&1),Sb=!!(Lb[0]>>26&1),Tb=!!(Lb[0]&4096);var ma=Qb?Sb:Kb(610401301,!1),lb=Qb?Rb||!Tb:Kb(748402147,!0);_.Ub=_.ba(a=>a!==null&&a!==void 0);var da,fa;da=_.ba(a=>typeof a==="number");_.ca=_.ba(a=>typeof a==="string");fa=_.ba(a=>typeof a==="boolean");_.Vb=_.ba(a=>!!a&&(typeof a==="object"||typeof a==="function"));_.Wb=_.ba(()=>!0);var ea=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Zb,Xb,$b,Yb;_.eb=_.ba(a=>ea?a>=Xb&&a<=Yb:a[0]==="-"?ia(a,Zb):ia(a,$b));Zb=Number.MIN_SAFE_INTEGER.toString();Xb=ea?BigInt(Number.MIN_SAFE_INTEGER):void 0;$b=Number.MAX_SAFE_INTEGER.toString();Yb=ea?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.ac=typeof TextDecoder!=="undefined";_.bc=typeof TextEncoder!=="undefined";var na,cc=_.t.navigator;na=cc?cc.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.dc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.ec=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.fc=function(a){_.fc[" "](a);return a};_.fc[" "]=function(){};var tc;_.hc=_.qa();_.ic=_.ra();_.jc=_.u("Edge");_.kc=_.u("Gecko")&&!(_.la()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.lc=_.la()&&!_.u("Edge");_.mc=_.ya();_.nc=va()?na.platform==="Windows":_.u("Windows");_.oc=va()?na.platform==="Android":_.u("Android");_.pc=wa();_.qc=_.u("iPad");_.rc=_.u("iPod");_.sc=_.xa();
a:{let a="",b=function(){var c=_.ka();if(_.kc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.jc)return/Edge\/([\d\.]+)/.exec(c);if(_.ic)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.lc)return/WebKit\/(\S+)/.exec(c);if(_.hc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ic){var uc;let c=_.t.document;uc=c?c.documentMode:void 0;if(uc!=null&&uc>parseFloat(a)){tc=String(uc);break a}}tc=a}_.vc=tc;_.wc=_.sa();_.xc=wa()||_.u("iPod");_.yc=_.u("iPad");_.zc=_.u("Android")&&!(ta()||_.sa()||_.qa()||_.u("Silk"));_.Ac=ta();_.Bc=_.ua()&&!_.xa();var $a,ob,Da,ib;_.Ya=_.Ca();_.Cc=_.Ca();$a=_.Ca();_.Dc=_.Ca();ob=_.Ca();Da=_.Ca("m_m",!0);ib=_.Ca();_.Ec=_.Ca();var Gc;_.v=_.Ca("jas",!0);Gc=[];Gc[_.v]=7;_.Fc=Object.freeze(Gc);var Ea,Ga;Ea={};Ga={};_.Hc=Object.freeze({});var jb={};var La=void 0;_.Ic=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Jc=Number.isSafeInteger;_.Qa=Number.isFinite;_.Kc=Math.trunc;var bb;_.Lc=_.ha(0);_.Mc={};_.Nc=function(a,b,c,d,e){b=_.yb(a.ma,b,c,e);if(b!==null||d&&a.A!==Ga)return b};_.yb=function(a,b,c,d){if(b===-1)return null;var e=b+(c?0:-1),f=a.length-1;if(!(f<1+(c?0:-1))){if(e>=f){var g=a[f];if(g!=null&&typeof g==="object"&&g.constructor===Object){c=g[b];var h=!0}else if(e===f)c=g;else return}else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Oc=function(a,b,c,d){_.vb(a);var e=a.ma;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){var e=a.ma,f=e[_.v]|0;b=_.zb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ha(a,f)){let g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.ma,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.H=function(a,b,c){c==null&&(c=void 0);_.Oc(a,b,c);c&&!_.Ha(c)&&_.wb(a.ma);return a};_.Pc=function(a,b,c,d){return _.Sa(_.Nc(a,b,c,d))};_.I=function(a,b,c=!1,d){var e;return(e=_.Pa(_.Nc(a,b,d)))!=null?e:c};_.J=function(a,b,c="",d){var e;return(e=_.Va(_.Nc(a,b,d)))!=null?e:c};
_.K=function(a,b,c){return _.Va(_.Nc(a,b,c,_.Mc))};_.L=function(a,b,c,d){return _.Oc(a,b,c==null?c:_.Oa(c),d)};_.M=function(a,b,c){return _.Oc(a,b,c==null?c:_.Ta(c))};_.N=function(a,b,c,d){return _.Oc(a,b,_.Ua(c),d)};_.O=function(a,b,c,d){return _.Oc(a,b,c==null?c:_.Ra(c),d)};_.P=class{constructor(a,b,c){this.ma=_.nb(a,b,c,2048)}toJSON(){return kb(this)}va(a){return JSON.stringify(kb(this,a))}};_.P.prototype[Da]=Ea;_.P.prototype.toString=function(){return this.ma.toString()};_.Qc=_.Ab();_.Rc=_.Ab();_.Sc=_.Ab();_.Tc=Symbol();var Uc=class extends _.P{constructor(a){super(a)}};_.Vc=class extends _.P{constructor(a){super(a)}G(a){return _.M(this,3,a)}};_.Wc=class extends _.P{constructor(a){super(a)}};_.x.prototype.wa=!1;_.x.prototype.isDisposed=function(){return this.wa};_.x.prototype.dispose=function(){this.wa||(this.wa=!0,this.T())};_.x.prototype[Symbol.dispose]=function(){this.dispose()};_.x.prototype.T=function(){if(this.ha)for(;this.ha.length;)this.ha.shift()()};var Xc=class extends _.x{constructor(){var a=window;super();this.A=a;this.j=[];this.v={}}resolve(a){var b=this.A;a=a.split(".");var c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}hc(){var a=this.j.length,b=this.j,c=[];for(let d=0;d<a;++d){let e=b[d].j(),f=this.resolve(e);if(f&&f!=this.v[e])try{b[d].hc(f)}catch(g){}else c.push(b[d])}this.j=c.concat(b.slice(a))}};var Zc=class extends _.x{constructor(){var a=_.Yc;super();this.A=a;this.C=this.j=null;this.B=0;this.D={};this.v=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.v=!0)}F(a,b){this.j=b;this.C=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.$c=class extends _.P{constructor(a){super(a)}};var ad=class extends _.P{constructor(a){super(a)}};var dd;_.bd=function(a,b,c=98,d=new _.Vc){if(a.j){let e=new Uc;_.N(e,1,b.message);_.N(e,2,b.stack);_.M(e,3,b.lineNumber);_.O(e,5,1);_.H(d,40,e);a.j.log(c,d)}};dd=class{constructor(){var a=cd;this.j=null;_.I(a,4,!0)}log(a,b=new _.Vc){_.bd(this,a,98,b)}};var ed,fd;ed=function(a){if(a.A.length>0){var b=a.j!==void 0,c=a.v!==void 0;if(b||c){b=b?a.B:a.C;c=a.A;a.A=[];try{_.dc(c,b,a)}catch(d){console.error(d)}}}};_.gd=class{constructor(a){this.j=a;this.v=void 0;this.A=[]}then(a,b,c){this.A.push(new fd(a,b,c));ed(this)}resolve(a){if(this.j!==void 0||this.v!==void 0)throw Error("v");this.j=a;ed(this)}reject(a){if(this.j!==void 0||this.v!==void 0)throw Error("v");this.v=a;ed(this)}B(a){a.v&&a.v.call(a.j,this.j)}C(a){a.A&&a.A.call(a.j,this.v)}};
fd=class{constructor(a,b,c){this.v=a;this.A=b;this.j=c}};_.hd=a=>{var b="Ec";if(a.Ec&&a.hasOwnProperty(b))return a.Ec;b=new a;return a.Ec=b};_.Q=class{constructor(){this.B=new _.gd;this.j=new _.gd;this.G=new _.gd;this.D=new _.gd;this.F=new _.gd;this.C=new _.gd;this.A=new _.gd;this.v=new _.gd;this.K=new _.gd;this.L=new _.gd;this.J=new _.gd}N(){return this.B}P(){return this.j}V(){return this.G}wa(){return this.D}R(){return this.F}O(){return this.C}M(){return this.A}ha(){return this.v}S(){return this.K}W(){return this.J}static j(){return _.hd(_.Q)}};var kd;_.jd=function(){return _.C(_.id,_.Wc,5)};kd=class extends _.P{constructor(a){super(a)}};var ld;window.gbar_&&window.gbar_.CONFIG?ld=window.gbar_.CONFIG[0]||{}:ld=[];_.id=new kd(ld);var cd;cd=_.C(_.id,ad,3)||new ad;_.Yc=new dd;_.A("gbar_._DumpException",function(a){_.Yc?_.Yc.log(a):console.error(a)});_.md=new Zc;var od;_.pd=function(a,b){var c=_.nd.j();if(a in c.j){if(c.j[a]!=b)throw new od;}else{c.j[a]=b;let h=c.v[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.j;delete b.j[a];if(_.Db(b.j)){for(var e=b.v.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.v[g]];b.A.apply(b.B,f)}}delete c.v[a]}};_.nd=class{constructor(){this.j={};this.v={}}static j(){return _.hd(_.nd)}};_.qd=class extends _.aa{constructor(){super()}};od=class extends _.qd{};_.A("gbar.A",_.gd);_.gd.prototype.aa=_.gd.prototype.then;_.A("gbar.B",_.Q);_.Q.prototype.ba=_.Q.prototype.P;_.Q.prototype.bb=_.Q.prototype.V;_.Q.prototype.bd=_.Q.prototype.R;_.Q.prototype.bf=_.Q.prototype.N;_.Q.prototype.bg=_.Q.prototype.wa;_.Q.prototype.bh=_.Q.prototype.O;_.Q.prototype.bj=_.Q.prototype.M;_.Q.prototype.bk=_.Q.prototype.ha;_.Q.prototype.bl=_.Q.prototype.S;_.Q.prototype.bm=_.Q.prototype.W;_.A("gbar.a",_.Q.j());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var rd=new Xc;
_.pd("api",rd);var sd=_.jd()||new _.Wc,td=window,ud=_.y(_.K(sd,8));td.__PVT=ud;_.pd("eq",_.md);
}catch(e){_._DumpException(e)}
try{
_.vd=class extends _.P{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var wd=class extends _.P{constructor(a){super(a)}};var xd=class extends _.x{constructor(){super();this.v=[];this.j=[]}A(a,b){this.v.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.y(_.K(a,1));_.Pa(_.Nc(a,12))!=null&&(d.dpo=_.Bb(_.I(a,12)));d.ms=_.y(_.K(a,2));d.m=_.y(_.K(a,3));d.l=[];_.J(b,1)&&(a=_.K(b,3))&&this.j.push(a);_.J(c,1)&&(c=_.K(c,2))&&this.j.push(c);_.A("gapi.load",(0,_.z)(this.A,this));return this}};var yd=_.C(_.id,_.$c,14);if(yd){var zd=_.C(_.id,_.vd,9)||new _.vd,Ad=new wd,Bd=new xd;Bd.init(yd,zd,Ad);_.pd("gs",Bd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_safdarshar6@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><link rel="stylesheet" href="./train_files/bundle.css"><script nonce="">var colabVersionTag = 'colab-external_20260902-060039_RC00_975032937'; var colabScsVersion = '430f6eb0746260b7aff6f3345c7fab04'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_prompt_cell\x22: true, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_user_input_char_limit\x22: 100000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_subpaths_in_kernel_url\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22assign_ping_hostname\x22: \x22https:\/\/ping.prod.colab.dev\x22, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22, \x22*.isolabs-kernels.corp.goog\x22, \x22*.proxy.googlers.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bluetooth\x22: true, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22cli_agent_colab_skills_folder_id\x22: \x221v81ndcRcnjykNnD4E_nLjhSZquEOntUY\x22, \x22cli_agent_file_manager\x22: false, \x22cli_agent_gemini_settings_file_id\x22: \x221fsqJkLe3Dt_YbgebQPg2HxFuGmz3O52m\x22, \x22cli_agent_md_file_id\x22: \x221pln3YuWkQQv_3AA7-QRygtXZid4hKUUs\x22, \x22cli_agent_root_dir\x22: \x22\/root\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_client_events_context\x22: true, \x22composer_compaction_interval\x22: 0, \x22composer_compaction_overlap_size\x22: 0, \x22composer_context_max_variable_length\x22: 500000, \x22composer_custom_context\x22: true, \x22composer_default_dock_right\x22: true, \x22composer_default_gemini_3_5_flash\x22: true, \x22composer_default_gemini_3_flash\x22: false, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_enable_gemini_3_5_flash\x22: true, \x22composer_enable_gemini_3_5_flash_consumer\x22: false, \x22composer_enable_gemini_3_5_flash_external\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_generate_code\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_remove_gemini_3_0_flash_consumer\x22: false, \x22composer_replace_empty_cells_when_adding_new_cells\x22: true, \x22composer_runtime_profile_in_context\x22: false, \x22composer_show_debug_info\x22: false, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22composer_visualization_mode\x22: true, \x22composer_visualization_mode_bypass_accept\x22: false, \x22connect_enterprise_vm\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22critique_comments\x22: false, \x22data_inspector\x22: true, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_antigravity_cli\x22: false, \x22enable_bigquery_data_explorer\x22: false, \x22enable_bigquery_easy_gcp_project_creation\x22: false, \x22enable_colab_mcp_integration\x22: true, \x22enable_colab_mcp_showdiff\x22: false, \x22enable_composer_code_report\x22: false, \x22enable_composer_ds_star\x22: false, \x22enable_composer_floating_spark_off\x22: false, \x22enable_composer_fp_orcas_integration_v2\x22: false, \x22enable_composer_generated_cell_insertion_position\x22: true, \x22enable_composer_quota_ui\x22: true, \x22enable_composer_skills\x22: false, \x22enable_composer_suggestion_chips\x22: true, \x22enable_composer_text_cell_transformations\x22: true, \x22enable_composer_tools_default_on\x22: false, \x22enable_dsa_agent_steps_bundle\x22: true, \x22enable_fp_user_provided_context_links\x22: false, \x22enable_gcp_preferences\x22: false, \x22enable_google_one_ui\x22: true, \x22enable_iframe_unloading\x22: true, \x22enable_increased_composer_thinking\x22: false, \x22enable_ipynb_utils_refactor\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_public_api_vscode\x22: true, \x22enable_quota_dark_launch\x22: true, \x22enable_rt_on_create\x22: false, \x22enable_shorten_system_instructions\x22: true, \x22enable_ssh_access\x22: true, \x22enable_vs_code_drive_import\x22: false, \x22enable_vs_code_drive_import_file_menu\x22: false, \x22enable_vscode_telemetry\x22: true, \x22enable_web_mcp\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22google_one_eligible_countries\x22: \x5b\x22US\x22, \x22CA\x22, \x22MX\x22\x5d, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jsraw\x22: \x22es6\x22, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_cloud_onboarding_client\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_create_assignment\x22: true, \x22migrate_get_assignment\x22: true, \x22migrate_recaptcha_poll\x22: true, \x22migrate_recaptcha_submit\x22: true, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22optimize_composer_context_order\x22: false, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22preference_deep_equality_check\x22: true, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_composer_planning_overeagerness\x22: true, \x22refresh_warning_timeout_ms\x22: 604800000, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rpc_for_payments_signing\x22: false, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222026.07\x22, \x222026.04\x22, \x222026.01\x22, \x222025.10\x22, \x222025.07\x22\x5d, \x22search_by_content\x22: true, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: false, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_switch_to_prod_link\x22: false, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22snippets_ui_refresh\x22: false, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_timeout_ms\x22: 300000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22thinking_budget\x22: -1, \x22tos_consent_override\x22: false, \x22tos_v6\x22: true, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22trim_filename_extension\x22: false, \x22truncate_composer_execution_results\x22: true, \x22turn_off_agent_mode_when_safe\x22: true, \x22ui_demo_id\x22: \x22\x22, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_jetski_prod_composer\x22: false, \x22use_kernel_state_metadata_adk\x22: false, \x22use_kkb_if_configured\x22: false, \x22use_refactored_constraints\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22G4\x22, \x22H100\x22, \x22L4\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_composer_tools\x22: \x5b\x5d, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22ids\x22: \x5b20730550, 20730681, 20730766, 20730457, 20730460, 20730837, 20730863, 20730685, 20730693, 20730750, 20730770, 20730556, 20730831, 20730640, 20730660, 20730559, 20730183\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22assign_ping_hostname\x22: 45747049, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bluetooth\x22: 45791828, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classroom_iframe_parent_origin\x22: 45425537, \x22cli_agent_colab_skills_folder_id\x22: 45780872, \x22cli_agent_file_manager\x22: 45781533, \x22cli_agent_gemini_settings_file_id\x22: 45780871, \x22cli_agent_md_file_id\x22: 45780870, \x22cli_agent_root_dir\x22: 45780873, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_client_events_context\x22: 45729342, \x22composer_compaction_interval\x22: 45749782, \x22composer_compaction_overlap_size\x22: 45749781, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_custom_context\x22: 45728743, \x22composer_default_dock_right\x22: 45755037, \x22composer_default_gemini_3_5_flash\x22: 45800193, \x22composer_default_gemini_3_flash\x22: 45785126, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_enable_gemini_3_5_flash\x22: 45800582, \x22composer_enable_gemini_3_5_flash_consumer\x22: 45834949, \x22composer_enable_gemini_3_5_flash_external\x22: 45823584, \x22composer_focused_cell_context\x22: 45697545, \x22composer_generate_code\x22: 45702500, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_remove_gemini_3_0_flash_consumer\x22: 45835039, \x22composer_replace_empty_cells_when_adding_new_cells\x22: 45788233, \x22composer_runtime_profile_in_context\x22: 45796713, \x22composer_show_debug_info\x22: 45700003, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22composer_visualization_mode\x22: 45774882, \x22composer_visualization_mode_bypass_accept\x22: 45777833, \x22connect_enterprise_vm\x22: 45730782, \x22converse_notebook_context_length\x22: 45705427, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22embedded_use_websockets\x22: 45691694, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_antigravity_cli\x22: 45835367, \x22enable_bigquery_data_explorer\x22: 45765771, \x22enable_bigquery_easy_gcp_project_creation\x22: 45775926, \x22enable_colab_mcp_integration\x22: 45741279, \x22enable_colab_mcp_showdiff\x22: 45768032, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_ds_star\x22: 45779762, \x22enable_composer_floating_spark_off\x22: 45771195, \x22enable_composer_fp_orcas_integration_v2\x22: 45758361, \x22enable_composer_generated_cell_insertion_position\x22: 45763491, \x22enable_composer_quota_ui\x22: 45790572, \x22enable_composer_skills\x22: 45778172, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_composer_text_cell_transformations\x22: 45758370, \x22enable_composer_tools_default_on\x22: 45780469, \x22enable_dsa_agent_steps_bundle\x22: 45755666, \x22enable_fp_user_provided_context_links\x22: 45746774, \x22enable_gcp_preferences\x22: 45762481, \x22enable_google_one_ui\x22: 45796167, \x22enable_iframe_unloading\x22: 45765934, \x22enable_increased_composer_thinking\x22: 45792521, \x22enable_ipynb_utils_refactor\x22: 45803524, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_public_api_vscode\x22: 45802393, \x22enable_quota_dark_launch\x22: 45785072, \x22enable_rt_on_create\x22: 45667583, \x22enable_shorten_system_instructions\x22: 45778351, \x22enable_ssh_access\x22: 45806462, \x22enable_vs_code_drive_import\x22: 45775679, \x22enable_vs_code_drive_import_file_menu\x22: 45775758, \x22enable_vscode_telemetry\x22: 45760437, \x22enable_web_mcp\x22: 45769687, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22github_client_id\x22: 45425556, \x22google_one_eligible_countries\x22: 45828507, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_cloud_onboarding_client\x22: 45784102, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_create_assignment\x22: 45795779, \x22migrate_get_assignment\x22: 45784121, \x22migrate_recaptcha_poll\x22: 45781390, \x22migrate_recaptcha_submit\x22: 45787881, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22optimize_composer_context_order\x22: 45759155, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22preference_deep_equality_check\x22: 45740961, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_composer_planning_overeagerness\x22: 45758628, \x22refresh_warning_timeout_ms\x22: 45765093, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rpc_for_payments_signing\x22: 45797300, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22search_by_content\x22: 45778175, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_switch_to_prod_link\x22: 45425483, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22snippets_ui_refresh\x22: 45737461, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22thinking_budget\x22: 45784302, \x22tos_consent_override\x22: 45817659, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22trim_filename_extension\x22: 45691676, \x22truncate_composer_execution_results\x22: 45746694, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22ui_demo_id\x22: 45784115, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_jetski_prod_composer\x22: 45801236, \x22use_kernel_state_metadata_adk\x22: 45737477, \x22use_kkb_if_configured\x22: 45733350, \x22use_refactored_constraints\x22: 45740233, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_composer_tools\x22: 45752901, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138\x7d\x7d'); var colabUserEmail = 'safdarshar6@gmail.com'; var colabRenderDataToken = 'AFWLbD1stz-DQp8hbZ-Jiirq-jz88i90MYBU3YoAN2P819nvFUWj11Vq7cJTZet2eNnKJXCiR7YiNE12bVU3mVdn4gviLpl1M0pHAvP3sybinQqB'; var colabConfig = '\x5b\x5b\x22safdarshar6@gmail.com\x22,\x5b1,\x22AHXL0D2FyfJ4IFzdO54TkhAwmxQ1LUx\/2HTXyos75QlBDPt+1Tc5xccG8i2eUiOKBcvoTwSNjtc58ow23GczlT0ZpgT+3eMQy7z66GzaP97lGGtR9qJj\/prkNFXSF0t5Dlv23WKb4zxsvX6NQ5Rp\/TNLV\/sdnKvc6L90nhxPH8UEEweMNlV\/c+9uJ4CIGeB+f3VQyzNtI8wVL0N8EeFIXIxaCbPkocs1frNvqoBfvVMydM+08LFPzsdvKSg72S5lVuhSal5NQ57qqzCXzijSkp5hnkL5JS7ghomoSZaCVmQddgbB64qFpBZu\/H56ks+fLXe\/dSWfJdZYWYBLdgyLCHCMTJ61fdthu0bRzyqaw71Sgy+7McYKBKLTkyhmbyebvkdEqhOlhi+azwQwVihHwuRynDQBNQLz+dw0cnHSjeTcmIPp2Dx7HGOF+wgE4lHGU3YQ5STHWS2pg5NGh7FfqF59Nrey+B6SbokVVE6HUj0k37i5nNOKos3hpYZopO9uQm+eaKMw3YsDcF7\/nAM1RnEiOTNjRc9Hd4X6L19pj\/h+HgvdYHXLrpaZcsR2dVR45y\/yTUfNFt1eVbiiIUQNkuKd446QI7oKcnr7Icsoe7JbtnZcQvdOlhpn44u+98qTCrPqJNy4y1VX1jrmeFnMGliFq4j1PjrVL+GxDSZewGhrWG1h1P6lNYNHd4il\/CldyCyD2OYNTNGKX80s298ytT9cYYSjwIFE1YBZPmNLq1dhD7F9Opf+CcK1wMlSD\/rTqFNmxtNcJkPOXGjnjB6038xvbV6Df1Y6qHZsvdRv+SW\/9X8WQjJ9P74qG3jUqwqXdqovUGsYqjo1sPj7Yq11auhCXLCS\/z76oeMR2FhBLBimSLKzKUWDVJ1QqMBfhLufIccoPidE9JsAEa7o90\/pC5QuFFGgi\/5ojsUerDH0QoQumwR1\/FbqoAYTUHv1ZMXBtG8X72O34I5nza7eRrwHZDA8eJn4FDGgNKo\/W+3+fk3mzjPqrARclNfrJv+QHUXjXkW+w1I2z+Z\/0neFsMeOqPdtlT73me5ZQ5K7yKNK72CMFYeYKyS0B7PKRr8AR2rtdeoyq+Yk3wUvGaLuIK1gTWUoHKCI+72H+zGyCzFBCSGB2D\/UkNpi07Pa9jwGt3lb8HqOqSxly7KR+hCfZ+VyjO8ZUr8efS2G9JshDhE9K24h7JiCtQgcof3qxuSlZEtHX\/4Au+dQ8MTFLLA8+17HrNp7HeBW0hIu9kvXcr3oKG7Mm1LLejfNsDYtK4NJpTCRqm5+1VYUij6Jhded5Q4nx6Lb6M5MplcbCkm7y\/hVrX+431eKB5Illocxh6SmBpLqhtEF44ZoOFCWvCwqqYQZKbVuYdEws5kIaW4zTHqVnP+Y\/5VVl9tuR8a7pdvXWRh0uIoy6oSQCWGH3\/gT4Q+wPM6hJDkuPhX\/i3+3ko2gKsGV4Dtif6qG7FO8lZ6v81vuKL9Og\/JlzWKB6kU6Ckc3Lj7x0HPGDJdcq3ldpmUyQwHnFXaejHdSanccTjfXqkp4lUr1gGXo0z+h9STqVq7EkPX1XsVXYIJz\/k8sMYaMDTnTZ6C1QWR7PdMGLEN6LKOWfKgct7RK\/ZsfNSxRymEjbiUwLRRAV6wuCiwzk52mw\/D9VmuRKqg5g1ziJ\/SaSxt0VTR8zbIiR0GfA231KPw6QcFrbEnUDmZcRKFDumSH+LzjJiKD9KZ8nUCOdEtfJseI3Mz9\/YA0S9cd2B81ZzlBWMsZEY4FkqLZ1DCFJr4GZh2j4aZ4zbwlwr00zGKc3unYjDmzLRMq54JavvtPC7kdm1WiuzjsI4aZHFG+2bwPl4GuG2FNzWf6DGe2brWIMAclSv635VXW1dzTtRMGUIGfIpOn76ayypmXM2jhAS6UCmNcdfybn2qN+9Jujv43yFyY5Uu9V16rHa8MW2ki9n1dmkupFv\/8DuB+8zam+VCinwtPiNn4+BUy1ErkbAahp6Qi4DhIJK4Z+8Zv\x22,\x22AJ9oCCwdZqRTAL1X6BJE2Moa6nrrjlNbyXmDug5PUmIGGLdPSpQnD2Z3ND7Zw47CsUAtFXxKP+SgMsHlr+xUCxGQeI0gqjekbXZtLEfj87fBQ+bhg8yAR1EVOJA8DiGMNnjoL79PuTvk\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$ 9.99\x22,\x22$ 49.99\x22,\x22$ 9.99\x22,\x22$ 49.99\x22,0,0,0,0,0,0,0\x5d,\x5b1,5,8\x5d,\x22PK\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/430f6eb0746260b7aff6f3345c7fab04/img%2Ffavicon.ico"><meta name="google-site-verification" content="h4AyILcMXlXf3PDJKg3Fu2_dyS3jfH5im5G__oDgjOs"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="gl3hNNVi7GnXImkDiRAkUxkhUD4g7Ke8L4D6Ve8FEVY"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="HwWGKCyRK7kxGyAlA30sbbTly9VW0SOM7Sh4juqiOVA"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta name="google-site-verification" content="3tGzCQxLejik3-Q5npF5QDCXrVwAFP3xN4n6tWBBnGM"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script src="./train_files/api.js.download" nonce="" gapi_processed="true"></script><script async="" src="./train_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./train_files/rs=AA2YrTuJWwymoLzabh5d8DnMJYz1k9It3Q" nonce=""></script><link type="text/css" href="./train_files/rs=AA2YrTvWGogfe9gNdtCZFN4PB5nWDEkvlA" rel="stylesheet"><link id="oaas-sdk-warmup" href="https://console.cloud.google.com/" rel="preconnect" crossorigin="use-credentials"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./train_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./train_files/editor.main.css"><script src="./train_files/api(1).js.download" nonce=""></script><script src="./train_files/api(2).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-git-pull-request-label:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-terminal-decoration-success:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-terminal-decoration-incomplete:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-diff-sidebyside:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-git-pull-request-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-terminal-decoration-mark:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-git-pull-request-reviewer:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-git-pull-request-assignee:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unknown:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-terminal-decoration-error:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-blank:before { content: '\ec03'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-horizontal:before { content: '\ec05'; }
.codicon-fold-horizontal:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-map-horizontal-filled:before { content: '\ec06'; }
.codicon-fold-horizontal-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-mic:before { content: '\ec12'; }
.codicon-thumbsdown-filled:before { content: '\ec13'; }
.codicon-thumbsup-filled:before { content: '\ec14'; }
.codicon-coffee:before { content: '\ec15'; }
.codicon-snake:before { content: '\ec16'; }
.codicon-game:before { content: '\ec17'; }
.codicon-vr:before { content: '\ec18'; }
.codicon-chip:before { content: '\ec19'; }
.codicon-piano:before { content: '\ec1a'; }
.codicon-music:before { content: '\ec1b'; }
.codicon-mic-filled:before { content: '\ec1c'; }
.codicon-repo-fetch:before { content: '\ec1d'; }
.codicon-copilot:before { content: '\ec1e'; }
.codicon-lightbulb-sparkle:before { content: '\ec1f'; }
.codicon-robot:before { content: '\ec20'; }
.codicon-sparkle-filled:before { content: '\ec21'; }
.codicon-diff-single:before { content: '\ec22'; }
.codicon-diff-multiple:before { content: '\ec23'; }
.codicon-surround-with:before { content: '\ec24'; }
.codicon-share:before { content: '\ec25'; }
.codicon-git-stash:before { content: '\ec26'; }
.codicon-git-stash-apply:before { content: '\ec27'; }
.codicon-git-stash-pop:before { content: '\ec28'; }
.codicon-vscode:before { content: '\ec29'; }
.codicon-vscode-insiders:before { content: '\ec2a'; }
.codicon-code-oss:before { content: '\ec2b'; }
.codicon-run-coverage:before { content: '\ec2c'; }
.codicon-run-all-coverage:before { content: '\ec2d'; }
.codicon-coverage:before { content: '\ec2e'; }
.codicon-github-project:before { content: '\ec2f'; }
.codicon-map-vertical:before { content: '\ec30'; }
.codicon-fold-vertical:before { content: '\ec30'; }
.codicon-map-vertical-filled:before { content: '\ec31'; }
.codicon-fold-vertical-filled:before { content: '\ec31'; }
.codicon-go-to-search:before { content: '\ec32'; }
.codicon-percentage:before { content: '\ec33'; }
.codicon-sort-percentage:before { content: '\ec33'; }
.codicon-attach:before { content: '\ec34'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-git-fetch:before { content: '\ec1d'; }
.codicon-lightbulb-sparkle-autofix:before { content: '\ec1f'; }
.codicon-debug-breakpoint-pending:before { content: '\ebd9'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-hover-increase-verbosity:before { content: '\ea60'; }
.codicon-hover-decrease-verbosity:before { content: '\eb3b'; }
.codicon-gutter-lightbulb:before { content: '\ea61'; }
.codicon-gutter-lightbulb-auto-fix:before { content: '\eb13'; }
.codicon-gutter-lightbulb-sparkle:before { content: '\ec1f'; }
.codicon-gutter-lightbulb-aifix-auto-fix:before { content: '\ec1f'; }
.codicon-gutter-lightbulb-sparkle-filled:before { content: '\ec21'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
:root { --vscode-icon-add-content: '\ea60'; --vscode-icon-add-font-family: 'codicon'; --vscode-icon-plus-content: '\ea60'; --vscode-icon-plus-font-family: 'codicon'; --vscode-icon-gist-new-content: '\ea60'; --vscode-icon-gist-new-font-family: 'codicon'; --vscode-icon-repo-create-content: '\ea60'; --vscode-icon-repo-create-font-family: 'codicon'; --vscode-icon-lightbulb-content: '\ea61'; --vscode-icon-lightbulb-font-family: 'codicon'; --vscode-icon-light-bulb-content: '\ea61'; --vscode-icon-light-bulb-font-family: 'codicon'; --vscode-icon-repo-content: '\ea62'; --vscode-icon-repo-font-family: 'codicon'; --vscode-icon-repo-delete-content: '\ea62'; --vscode-icon-repo-delete-font-family: 'codicon'; --vscode-icon-gist-fork-content: '\ea63'; --vscode-icon-gist-fork-font-family: 'codicon'; --vscode-icon-repo-forked-content: '\ea63'; --vscode-icon-repo-forked-font-family: 'codicon'; --vscode-icon-git-pull-request-content: '\ea64'; --vscode-icon-git-pull-request-font-family: 'codicon'; --vscode-icon-git-pull-request-abandoned-content: '\ea64'; --vscode-icon-git-pull-request-abandoned-font-family: 'codicon'; --vscode-icon-record-keys-content: '\ea65'; --vscode-icon-record-keys-font-family: 'codicon'; --vscode-icon-keyboard-content: '\ea65'; --vscode-icon-keyboard-font-family: 'codicon'; --vscode-icon-tag-content: '\ea66'; --vscode-icon-tag-font-family: 'codicon'; --vscode-icon-git-pull-request-label-content: '\ea66'; --vscode-icon-git-pull-request-label-font-family: 'codicon'; --vscode-icon-tag-add-content: '\ea66'; --vscode-icon-tag-add-font-family: 'codicon'; --vscode-icon-tag-remove-content: '\ea66'; --vscode-icon-tag-remove-font-family: 'codicon'; --vscode-icon-person-content: '\ea67'; --vscode-icon-person-font-family: 'codicon'; --vscode-icon-person-follow-content: '\ea67'; --vscode-icon-person-follow-font-family: 'codicon'; --vscode-icon-person-outline-content: '\ea67'; --vscode-icon-person-outline-font-family: 'codicon'; --vscode-icon-person-filled-content: '\ea67'; --vscode-icon-person-filled-font-family: 'codicon'; --vscode-icon-git-branch-content: '\ea68'; --vscode-icon-git-branch-font-family: 'codicon'; --vscode-icon-git-branch-create-content: '\ea68'; --vscode-icon-git-branch-create-font-family: 'codicon'; --vscode-icon-git-branch-delete-content: '\ea68'; --vscode-icon-git-branch-delete-font-family: 'codicon'; --vscode-icon-source-control-content: '\ea68'; --vscode-icon-source-control-font-family: 'codicon'; --vscode-icon-mirror-content: '\ea69'; --vscode-icon-mirror-font-family: 'codicon'; --vscode-icon-mirror-public-content: '\ea69'; --vscode-icon-mirror-public-font-family: 'codicon'; --vscode-icon-star-content: '\ea6a'; --vscode-icon-star-font-family: 'codicon'; --vscode-icon-star-add-content: '\ea6a'; --vscode-icon-star-add-font-family: 'codicon'; --vscode-icon-star-delete-content: '\ea6a'; --vscode-icon-star-delete-font-family: 'codicon'; --vscode-icon-star-empty-content: '\ea6a'; --vscode-icon-star-empty-font-family: 'codicon'; --vscode-icon-comment-content: '\ea6b'; --vscode-icon-comment-font-family: 'codicon'; --vscode-icon-comment-add-content: '\ea6b'; --vscode-icon-comment-add-font-family: 'codicon'; --vscode-icon-alert-content: '\ea6c'; --vscode-icon-alert-font-family: 'codicon'; --vscode-icon-warning-content: '\ea6c'; --vscode-icon-warning-font-family: 'codicon'; --vscode-icon-search-content: '\ea6d'; --vscode-icon-search-font-family: 'codicon'; --vscode-icon-search-save-content: '\ea6d'; --vscode-icon-search-save-font-family: 'codicon'; --vscode-icon-log-out-content: '\ea6e'; --vscode-icon-log-out-font-family: 'codicon'; --vscode-icon-sign-out-content: '\ea6e'; --vscode-icon-sign-out-font-family: 'codicon'; --vscode-icon-log-in-content: '\ea6f'; --vscode-icon-log-in-font-family: 'codicon'; --vscode-icon-sign-in-content: '\ea6f'; --vscode-icon-sign-in-font-family: 'codicon'; --vscode-icon-eye-content: '\ea70'; --vscode-icon-eye-font-family: 'codicon'; --vscode-icon-eye-unwatch-content: '\ea70'; --vscode-icon-eye-unwatch-font-family: 'codicon'; --vscode-icon-eye-watch-content: '\ea70'; --vscode-icon-eye-watch-font-family: 'codicon'; --vscode-icon-circle-filled-content: '\ea71'; --vscode-icon-circle-filled-font-family: 'codicon'; --vscode-icon-primitive-dot-content: '\ea71'; --vscode-icon-primitive-dot-font-family: 'codicon'; --vscode-icon-close-dirty-content: '\ea71'; --vscode-icon-close-dirty-font-family: 'codicon'; --vscode-icon-debug-breakpoint-content: '\ea71'; --vscode-icon-debug-breakpoint-font-family: 'codicon'; --vscode-icon-debug-breakpoint-disabled-content: '\ea71'; --vscode-icon-debug-breakpoint-disabled-font-family: 'codicon'; --vscode-icon-debug-hint-content: '\ea71'; --vscode-icon-debug-hint-font-family: 'codicon'; --vscode-icon-terminal-decoration-success-content: '\ea71'; --vscode-icon-terminal-decoration-success-font-family: 'codicon'; --vscode-icon-primitive-square-content: '\ea72'; --vscode-icon-primitive-square-font-family: 'codicon'; --vscode-icon-edit-content: '\ea73'; --vscode-icon-edit-font-family: 'codicon'; --vscode-icon-pencil-content: '\ea73'; --vscode-icon-pencil-font-family: 'codicon'; --vscode-icon-info-content: '\ea74'; --vscode-icon-info-font-family: 'codicon'; --vscode-icon-issue-opened-content: '\ea74'; --vscode-icon-issue-opened-font-family: 'codicon'; --vscode-icon-gist-private-content: '\ea75'; --vscode-icon-gist-private-font-family: 'codicon'; --vscode-icon-git-fork-private-content: '\ea75'; --vscode-icon-git-fork-private-font-family: 'codicon'; --vscode-icon-lock-content: '\ea75'; --vscode-icon-lock-font-family: 'codicon'; --vscode-icon-mirror-private-content: '\ea75'; --vscode-icon-mirror-private-font-family: 'codicon'; --vscode-icon-close-content: '\ea76'; --vscode-icon-close-font-family: 'codicon'; --vscode-icon-remove-close-content: '\ea76'; --vscode-icon-remove-close-font-family: 'codicon'; --vscode-icon-x-content: '\ea76'; --vscode-icon-x-font-family: 'codicon'; --vscode-icon-repo-sync-content: '\ea77'; --vscode-icon-repo-sync-font-family: 'codicon'; --vscode-icon-sync-content: '\ea77'; --vscode-icon-sync-font-family: 'codicon'; --vscode-icon-clone-content: '\ea78'; --vscode-icon-clone-font-family: 'codicon'; --vscode-icon-desktop-download-content: '\ea78'; --vscode-icon-desktop-download-font-family: 'codicon'; --vscode-icon-beaker-content: '\ea79'; --vscode-icon-beaker-font-family: 'codicon'; --vscode-icon-microscope-content: '\ea79'; --vscode-icon-microscope-font-family: 'codicon'; --vscode-icon-vm-content: '\ea7a'; --vscode-icon-vm-font-family: 'codicon'; --vscode-icon-device-desktop-content: '\ea7a'; --vscode-icon-device-desktop-font-family: 'codicon'; --vscode-icon-file-content: '\ea7b'; --vscode-icon-file-font-family: 'codicon'; --vscode-icon-file-text-content: '\ea7b'; --vscode-icon-file-text-font-family: 'codicon'; --vscode-icon-more-content: '\ea7c'; --vscode-icon-more-font-family: 'codicon'; --vscode-icon-ellipsis-content: '\ea7c'; --vscode-icon-ellipsis-font-family: 'codicon'; --vscode-icon-kebab-horizontal-content: '\ea7c'; --vscode-icon-kebab-horizontal-font-family: 'codicon'; --vscode-icon-mail-reply-content: '\ea7d'; --vscode-icon-mail-reply-font-family: 'codicon'; --vscode-icon-reply-content: '\ea7d'; --vscode-icon-reply-font-family: 'codicon'; --vscode-icon-organization-content: '\ea7e'; --vscode-icon-organization-font-family: 'codicon'; --vscode-icon-organization-filled-content: '\ea7e'; --vscode-icon-organization-filled-font-family: 'codicon'; --vscode-icon-organization-outline-content: '\ea7e'; --vscode-icon-organization-outline-font-family: 'codicon'; --vscode-icon-new-file-content: '\ea7f'; --vscode-icon-new-file-font-family: 'codicon'; --vscode-icon-file-add-content: '\ea7f'; --vscode-icon-file-add-font-family: 'codicon'; --vscode-icon-new-folder-content: '\ea80'; --vscode-icon-new-folder-font-family: 'codicon'; --vscode-icon-file-directory-create-content: '\ea80'; --vscode-icon-file-directory-create-font-family: 'codicon'; --vscode-icon-trash-content: '\ea81'; --vscode-icon-trash-font-family: 'codicon'; --vscode-icon-trashcan-content: '\ea81'; --vscode-icon-trashcan-font-family: 'codicon'; --vscode-icon-history-content: '\ea82'; --vscode-icon-history-font-family: 'codicon'; --vscode-icon-clock-content: '\ea82'; --vscode-icon-clock-font-family: 'codicon'; --vscode-icon-folder-content: '\ea83'; --vscode-icon-folder-font-family: 'codicon'; --vscode-icon-file-directory-content: '\ea83'; --vscode-icon-file-directory-font-family: 'codicon'; --vscode-icon-symbol-folder-content: '\ea83'; --vscode-icon-symbol-folder-font-family: 'codicon'; --vscode-icon-logo-github-content: '\ea84'; --vscode-icon-logo-github-font-family: 'codicon'; --vscode-icon-mark-github-content: '\ea84'; --vscode-icon-mark-github-font-family: 'codicon'; --vscode-icon-github-content: '\ea84'; --vscode-icon-github-font-family: 'codicon'; --vscode-icon-terminal-content: '\ea85'; --vscode-icon-terminal-font-family: 'codicon'; --vscode-icon-console-content: '\ea85'; --vscode-icon-console-font-family: 'codicon'; --vscode-icon-repl-content: '\ea85'; --vscode-icon-repl-font-family: 'codicon'; --vscode-icon-zap-content: '\ea86'; --vscode-icon-zap-font-family: 'codicon'; --vscode-icon-symbol-event-content: '\ea86'; --vscode-icon-symbol-event-font-family: 'codicon'; --vscode-icon-error-content: '\ea87'; --vscode-icon-error-font-family: 'codicon'; --vscode-icon-stop-content: '\ea87'; --vscode-icon-stop-font-family: 'codicon'; --vscode-icon-variable-content: '\ea88'; --vscode-icon-variable-font-family: 'codicon'; --vscode-icon-symbol-variable-content: '\ea88'; --vscode-icon-symbol-variable-font-family: 'codicon'; --vscode-icon-array-content: '\ea8a'; --vscode-icon-array-font-family: 'codicon'; --vscode-icon-symbol-array-content: '\ea8a'; --vscode-icon-symbol-array-font-family: 'codicon'; --vscode-icon-symbol-module-content: '\ea8b'; --vscode-icon-symbol-module-font-family: 'codicon'; --vscode-icon-symbol-package-content: '\ea8b'; --vscode-icon-symbol-package-font-family: 'codicon'; --vscode-icon-symbol-namespace-content: '\ea8b'; --vscode-icon-symbol-namespace-font-family: 'codicon'; --vscode-icon-symbol-object-content: '\ea8b'; --vscode-icon-symbol-object-font-family: 'codicon'; --vscode-icon-symbol-method-content: '\ea8c'; --vscode-icon-symbol-method-font-family: 'codicon'; --vscode-icon-symbol-function-content: '\ea8c'; --vscode-icon-symbol-function-font-family: 'codicon'; --vscode-icon-symbol-constructor-content: '\ea8c'; --vscode-icon-symbol-constructor-font-family: 'codicon'; --vscode-icon-symbol-boolean-content: '\ea8f'; --vscode-icon-symbol-boolean-font-family: 'codicon'; --vscode-icon-symbol-null-content: '\ea8f'; --vscode-icon-symbol-null-font-family: 'codicon'; --vscode-icon-symbol-numeric-content: '\ea90'; --vscode-icon-symbol-numeric-font-family: 'codicon'; --vscode-icon-symbol-number-content: '\ea90'; --vscode-icon-symbol-number-font-family: 'codicon'; --vscode-icon-symbol-structure-content: '\ea91'; --vscode-icon-symbol-structure-font-family: 'codicon'; --vscode-icon-symbol-struct-content: '\ea91'; --vscode-icon-symbol-struct-font-family: 'codicon'; --vscode-icon-symbol-parameter-content: '\ea92'; --vscode-icon-symbol-parameter-font-family: 'codicon'; --vscode-icon-symbol-type-parameter-content: '\ea92'; --vscode-icon-symbol-type-parameter-font-family: 'codicon'; --vscode-icon-symbol-key-content: '\ea93'; --vscode-icon-symbol-key-font-family: 'codicon'; --vscode-icon-symbol-text-content: '\ea93'; --vscode-icon-symbol-text-font-family: 'codicon'; --vscode-icon-symbol-reference-content: '\ea94'; --vscode-icon-symbol-reference-font-family: 'codicon'; --vscode-icon-go-to-file-content: '\ea94'; --vscode-icon-go-to-file-font-family: 'codicon'; --vscode-icon-symbol-enum-content: '\ea95'; --vscode-icon-symbol-enum-font-family: 'codicon'; --vscode-icon-symbol-value-content: '\ea95'; --vscode-icon-symbol-value-font-family: 'codicon'; --vscode-icon-symbol-ruler-content: '\ea96'; --vscode-icon-symbol-ruler-font-family: 'codicon'; --vscode-icon-symbol-unit-content: '\ea96'; --vscode-icon-symbol-unit-font-family: 'codicon'; --vscode-icon-activate-breakpoints-content: '\ea97'; --vscode-icon-activate-breakpoints-font-family: 'codicon'; --vscode-icon-archive-content: '\ea98'; --vscode-icon-archive-font-family: 'codicon'; --vscode-icon-arrow-both-content: '\ea99'; --vscode-icon-arrow-both-font-family: 'codicon'; --vscode-icon-arrow-down-content: '\ea9a'; --vscode-icon-arrow-down-font-family: 'codicon'; --vscode-icon-arrow-left-content: '\ea9b'; --vscode-icon-arrow-left-font-family: 'codicon'; --vscode-icon-arrow-right-content: '\ea9c'; --vscode-icon-arrow-right-font-family: 'codicon'; --vscode-icon-arrow-small-down-content: '\ea9d'; --vscode-icon-arrow-small-down-font-family: 'codicon'; --vscode-icon-arrow-small-left-content: '\ea9e'; --vscode-icon-arrow-small-left-font-family: 'codicon'; --vscode-icon-arrow-small-right-content: '\ea9f'; --vscode-icon-arrow-small-right-font-family: 'codicon'; --vscode-icon-arrow-small-up-content: '\eaa0'; --vscode-icon-arrow-small-up-font-family: 'codicon'; --vscode-icon-arrow-up-content: '\eaa1'; --vscode-icon-arrow-up-font-family: 'codicon'; --vscode-icon-bell-content: '\eaa2'; --vscode-icon-bell-font-family: 'codicon'; --vscode-icon-bold-content: '\eaa3'; --vscode-icon-bold-font-family: 'codicon'; --vscode-icon-book-content: '\eaa4'; --vscode-icon-book-font-family: 'codicon'; --vscode-icon-bookmark-content: '\eaa5'; --vscode-icon-bookmark-font-family: 'codicon'; --vscode-icon-debug-breakpoint-conditional-unverified-content: '\eaa6'; --vscode-icon-debug-breakpoint-conditional-unverified-font-family: 'codicon'; --vscode-icon-debug-breakpoint-conditional-content: '\eaa7'; --vscode-icon-debug-breakpoint-conditional-font-family: 'codicon'; --vscode-icon-debug-breakpoint-conditional-disabled-content: '\eaa7'; --vscode-icon-debug-breakpoint-conditional-disabled-font-family: 'codicon'; --vscode-icon-debug-breakpoint-data-unverified-content: '\eaa8'; --vscode-icon-debug-breakpoint-data-unverified-font-family: 'codicon'; --vscode-icon-debug-breakpoint-data-content: '\eaa9'; --vscode-icon-debug-breakpoint-data-font-family: 'codicon'; --vscode-icon-debug-breakpoint-data-disabled-content: '\eaa9'; --vscode-icon-debug-breakpoint-data-disabled-font-family: 'codicon'; --vscode-icon-debug-breakpoint-log-unverified-content: '\eaaa'; --vscode-icon-debug-breakpoint-log-unverified-font-family: 'codicon'; --vscode-icon-debug-breakpoint-log-content: '\eaab'; --vscode-icon-debug-breakpoint-log-font-family: 'codicon'; --vscode-icon-debug-breakpoint-log-disabled-content: '\eaab'; --vscode-icon-debug-breakpoint-log-disabled-font-family: 'codicon'; --vscode-icon-briefcase-content: '\eaac'; --vscode-icon-briefcase-font-family: 'codicon'; --vscode-icon-broadcast-content: '\eaad'; --vscode-icon-broadcast-font-family: 'codicon'; --vscode-icon-browser-content: '\eaae'; --vscode-icon-browser-font-family: 'codicon'; --vscode-icon-bug-content: '\eaaf'; --vscode-icon-bug-font-family: 'codicon'; --vscode-icon-calendar-content: '\eab0'; --vscode-icon-calendar-font-family: 'codicon'; --vscode-icon-case-sensitive-content: '\eab1'; --vscode-icon-case-sensitive-font-family: 'codicon'; --vscode-icon-check-content: '\eab2'; --vscode-icon-check-font-family: 'codicon'; --vscode-icon-checklist-content: '\eab3'; --vscode-icon-checklist-font-family: 'codicon'; --vscode-icon-chevron-down-content: '\eab4'; --vscode-icon-chevron-down-font-family: 'codicon'; --vscode-icon-chevron-left-content: '\eab5'; --vscode-icon-chevron-left-font-family: 'codicon'; --vscode-icon-chevron-right-content: '\eab6'; --vscode-icon-chevron-right-font-family: 'codicon'; --vscode-icon-chevron-up-content: '\eab7'; --vscode-icon-chevron-up-font-family: 'codicon'; --vscode-icon-chrome-close-content: '\eab8'; --vscode-icon-chrome-close-font-family: 'codicon'; --vscode-icon-chrome-maximize-content: '\eab9'; --vscode-icon-chrome-maximize-font-family: 'codicon'; --vscode-icon-chrome-minimize-content: '\eaba'; --vscode-icon-chrome-minimize-font-family: 'codicon'; --vscode-icon-chrome-restore-content: '\eabb'; --vscode-icon-chrome-restore-font-family: 'codicon'; --vscode-icon-circle-outline-content: '\eabc'; --vscode-icon-circle-outline-font-family: 'codicon'; --vscode-icon-circle-content: '\eabc'; --vscode-icon-circle-font-family: 'codicon'; --vscode-icon-debug-breakpoint-unverified-content: '\eabc'; --vscode-icon-debug-breakpoint-unverified-font-family: 'codicon'; --vscode-icon-terminal-decoration-incomplete-content: '\eabc'; --vscode-icon-terminal-decoration-incomplete-font-family: 'codicon'; --vscode-icon-circle-slash-content: '\eabd'; --vscode-icon-circle-slash-font-family: 'codicon'; --vscode-icon-circuit-board-content: '\eabe'; --vscode-icon-circuit-board-font-family: 'codicon'; --vscode-icon-clear-all-content: '\eabf'; --vscode-icon-clear-all-font-family: 'codicon'; --vscode-icon-clippy-content: '\eac0'; --vscode-icon-clippy-font-family: 'codicon'; --vscode-icon-close-all-content: '\eac1'; --vscode-icon-close-all-font-family: 'codicon'; --vscode-icon-cloud-download-content: '\eac2'; --vscode-icon-cloud-download-font-family: 'codicon'; --vscode-icon-cloud-upload-content: '\eac3'; --vscode-icon-cloud-upload-font-family: 'codicon'; --vscode-icon-code-content: '\eac4'; --vscode-icon-code-font-family: 'codicon'; --vscode-icon-collapse-all-content: '\eac5'; --vscode-icon-collapse-all-font-family: 'codicon'; --vscode-icon-color-mode-content: '\eac6'; --vscode-icon-color-mode-font-family: 'codicon'; --vscode-icon-comment-discussion-content: '\eac7'; --vscode-icon-comment-discussion-font-family: 'codicon'; --vscode-icon-credit-card-content: '\eac9'; --vscode-icon-credit-card-font-family: 'codicon'; --vscode-icon-dash-content: '\eacc'; --vscode-icon-dash-font-family: 'codicon'; --vscode-icon-dashboard-content: '\eacd'; --vscode-icon-dashboard-font-family: 'codicon'; --vscode-icon-database-content: '\eace'; --vscode-icon-database-font-family: 'codicon'; --vscode-icon-debug-continue-content: '\eacf'; --vscode-icon-debug-continue-font-family: 'codicon'; --vscode-icon-debug-disconnect-content: '\ead0'; --vscode-icon-debug-disconnect-font-family: 'codicon'; --vscode-icon-debug-pause-content: '\ead1'; --vscode-icon-debug-pause-font-family: 'codicon'; --vscode-icon-debug-restart-content: '\ead2'; --vscode-icon-debug-restart-font-family: 'codicon'; --vscode-icon-debug-start-content: '\ead3'; --vscode-icon-debug-start-font-family: 'codicon'; --vscode-icon-debug-step-into-content: '\ead4'; --vscode-icon-debug-step-into-font-family: 'codicon'; --vscode-icon-debug-step-out-content: '\ead5'; --vscode-icon-debug-step-out-font-family: 'codicon'; --vscode-icon-debug-step-over-content: '\ead6'; --vscode-icon-debug-step-over-font-family: 'codicon'; --vscode-icon-debug-stop-content: '\ead7'; --vscode-icon-debug-stop-font-family: 'codicon'; --vscode-icon-debug-content: '\ead8'; --vscode-icon-debug-font-family: 'codicon'; --vscode-icon-device-camera-video-content: '\ead9'; --vscode-icon-device-camera-video-font-family: 'codicon'; --vscode-icon-device-camera-content: '\eada'; --vscode-icon-device-camera-font-family: 'codicon'; --vscode-icon-device-mobile-content: '\eadb'; --vscode-icon-device-mobile-font-family: 'codicon'; --vscode-icon-diff-added-content: '\eadc'; --vscode-icon-diff-added-font-family: 'codicon'; --vscode-icon-diff-ignored-content: '\eadd'; --vscode-icon-diff-ignored-font-family: 'codicon'; --vscode-icon-diff-modified-content: '\eade'; --vscode-icon-diff-modified-font-family: 'codicon'; --vscode-icon-diff-removed-content: '\eadf'; --vscode-icon-diff-removed-font-family: 'codicon'; --vscode-icon-diff-renamed-content: '\eae0'; --vscode-icon-diff-renamed-font-family: 'codicon'; --vscode-icon-diff-content: '\eae1'; --vscode-icon-diff-font-family: 'codicon'; --vscode-icon-diff-sidebyside-content: '\eae1'; --vscode-icon-diff-sidebyside-font-family: 'codicon'; --vscode-icon-discard-content: '\eae2'; --vscode-icon-discard-font-family: 'codicon'; --vscode-icon-editor-layout-content: '\eae3'; --vscode-icon-editor-layout-font-family: 'codicon'; --vscode-icon-empty-window-content: '\eae4'; --vscode-icon-empty-window-font-family: 'codicon'; --vscode-icon-exclude-content: '\eae5'; --vscode-icon-exclude-font-family: 'codicon'; --vscode-icon-extensions-content: '\eae6'; --vscode-icon-extensions-font-family: 'codicon'; --vscode-icon-eye-closed-content: '\eae7'; --vscode-icon-eye-closed-font-family: 'codicon'; --vscode-icon-file-binary-content: '\eae8'; --vscode-icon-file-binary-font-family: 'codicon'; --vscode-icon-file-code-content: '\eae9'; --vscode-icon-file-code-font-family: 'codicon'; --vscode-icon-file-media-content: '\eaea'; --vscode-icon-file-media-font-family: 'codicon'; --vscode-icon-file-pdf-content: '\eaeb'; --vscode-icon-file-pdf-font-family: 'codicon'; --vscode-icon-file-submodule-content: '\eaec'; --vscode-icon-file-submodule-font-family: 'codicon'; --vscode-icon-file-symlink-directory-content: '\eaed'; --vscode-icon-file-symlink-directory-font-family: 'codicon'; --vscode-icon-file-symlink-file-content: '\eaee'; --vscode-icon-file-symlink-file-font-family: 'codicon'; --vscode-icon-file-zip-content: '\eaef'; --vscode-icon-file-zip-font-family: 'codicon'; --vscode-icon-files-content: '\eaf0'; --vscode-icon-files-font-family: 'codicon'; --vscode-icon-filter-content: '\eaf1'; --vscode-icon-filter-font-family: 'codicon'; --vscode-icon-flame-content: '\eaf2'; --vscode-icon-flame-font-family: 'codicon'; --vscode-icon-fold-down-content: '\eaf3'; --vscode-icon-fold-down-font-family: 'codicon'; --vscode-icon-fold-up-content: '\eaf4'; --vscode-icon-fold-up-font-family: 'codicon'; --vscode-icon-fold-content: '\eaf5'; --vscode-icon-fold-font-family: 'codicon'; --vscode-icon-folder-active-content: '\eaf6'; --vscode-icon-folder-active-font-family: 'codicon'; --vscode-icon-folder-opened-content: '\eaf7'; --vscode-icon-folder-opened-font-family: 'codicon'; --vscode-icon-gear-content: '\eaf8'; --vscode-icon-gear-font-family: 'codicon'; --vscode-icon-gift-content: '\eaf9'; --vscode-icon-gift-font-family: 'codicon'; --vscode-icon-gist-secret-content: '\eafa'; --vscode-icon-gist-secret-font-family: 'codicon'; --vscode-icon-gist-content: '\eafb'; --vscode-icon-gist-font-family: 'codicon'; --vscode-icon-git-commit-content: '\eafc'; --vscode-icon-git-commit-font-family: 'codicon'; --vscode-icon-git-compare-content: '\eafd'; --vscode-icon-git-compare-font-family: 'codicon'; --vscode-icon-compare-changes-content: '\eafd'; --vscode-icon-compare-changes-font-family: 'codicon'; --vscode-icon-git-merge-content: '\eafe'; --vscode-icon-git-merge-font-family: 'codicon'; --vscode-icon-github-action-content: '\eaff'; --vscode-icon-github-action-font-family: 'codicon'; --vscode-icon-github-alt-content: '\eb00'; --vscode-icon-github-alt-font-family: 'codicon'; --vscode-icon-globe-content: '\eb01'; --vscode-icon-globe-font-family: 'codicon'; --vscode-icon-grabber-content: '\eb02'; --vscode-icon-grabber-font-family: 'codicon'; --vscode-icon-graph-content: '\eb03'; --vscode-icon-graph-font-family: 'codicon'; --vscode-icon-gripper-content: '\eb04'; --vscode-icon-gripper-font-family: 'codicon'; --vscode-icon-heart-content: '\eb05'; --vscode-icon-heart-font-family: 'codicon'; --vscode-icon-home-content: '\eb06'; --vscode-icon-home-font-family: 'codicon'; --vscode-icon-horizontal-rule-content: '\eb07'; --vscode-icon-horizontal-rule-font-family: 'codicon'; --vscode-icon-hubot-content: '\eb08'; --vscode-icon-hubot-font-family: 'codicon'; --vscode-icon-inbox-content: '\eb09'; --vscode-icon-inbox-font-family: 'codicon'; --vscode-icon-issue-reopened-content: '\eb0b'; --vscode-icon-issue-reopened-font-family: 'codicon'; --vscode-icon-issues-content: '\eb0c'; --vscode-icon-issues-font-family: 'codicon'; --vscode-icon-italic-content: '\eb0d'; --vscode-icon-italic-font-family: 'codicon'; --vscode-icon-jersey-content: '\eb0e'; --vscode-icon-jersey-font-family: 'codicon'; --vscode-icon-json-content: '\eb0f'; --vscode-icon-json-font-family: 'codicon'; --vscode-icon-kebab-vertical-content: '\eb10'; --vscode-icon-kebab-vertical-font-family: 'codicon'; --vscode-icon-key-content: '\eb11'; --vscode-icon-key-font-family: 'codicon'; --vscode-icon-law-content: '\eb12'; --vscode-icon-law-font-family: 'codicon'; --vscode-icon-lightbulb-autofix-content: '\eb13'; --vscode-icon-lightbulb-autofix-font-family: 'codicon'; --vscode-icon-link-external-content: '\eb14'; --vscode-icon-link-external-font-family: 'codicon'; --vscode-icon-link-content: '\eb15'; --vscode-icon-link-font-family: 'codicon'; --vscode-icon-list-ordered-content: '\eb16'; --vscode-icon-list-ordered-font-family: 'codicon'; --vscode-icon-list-unordered-content: '\eb17'; --vscode-icon-list-unordered-font-family: 'codicon'; --vscode-icon-live-share-content: '\eb18'; --vscode-icon-live-share-font-family: 'codicon'; --vscode-icon-loading-content: '\eb19'; --vscode-icon-loading-font-family: 'codicon'; --vscode-icon-location-content: '\eb1a'; --vscode-icon-location-font-family: 'codicon'; --vscode-icon-mail-read-content: '\eb1b'; --vscode-icon-mail-read-font-family: 'codicon'; --vscode-icon-mail-content: '\eb1c'; --vscode-icon-mail-font-family: 'codicon'; --vscode-icon-markdown-content: '\eb1d'; --vscode-icon-markdown-font-family: 'codicon'; --vscode-icon-megaphone-content: '\eb1e'; --vscode-icon-megaphone-font-family: 'codicon'; --vscode-icon-mention-content: '\eb1f'; --vscode-icon-mention-font-family: 'codicon'; --vscode-icon-milestone-content: '\eb20'; --vscode-icon-milestone-font-family: 'codicon'; --vscode-icon-git-pull-request-milestone-content: '\eb20'; --vscode-icon-git-pull-request-milestone-font-family: 'codicon'; --vscode-icon-mortar-board-content: '\eb21'; --vscode-icon-mortar-board-font-family: 'codicon'; --vscode-icon-move-content: '\eb22'; --vscode-icon-move-font-family: 'codicon'; --vscode-icon-multiple-windows-content: '\eb23'; --vscode-icon-multiple-windows-font-family: 'codicon'; --vscode-icon-mute-content: '\eb24'; --vscode-icon-mute-font-family: 'codicon'; --vscode-icon-no-newline-content: '\eb25'; --vscode-icon-no-newline-font-family: 'codicon'; --vscode-icon-note-content: '\eb26'; --vscode-icon-note-font-family: 'codicon'; --vscode-icon-octoface-content: '\eb27'; --vscode-icon-octoface-font-family: 'codicon'; --vscode-icon-open-preview-content: '\eb28'; --vscode-icon-open-preview-font-family: 'codicon'; --vscode-icon-package-content: '\eb29'; --vscode-icon-package-font-family: 'codicon'; --vscode-icon-paintcan-content: '\eb2a'; --vscode-icon-paintcan-font-family: 'codicon'; --vscode-icon-pin-content: '\eb2b'; --vscode-icon-pin-font-family: 'codicon'; --vscode-icon-play-content: '\eb2c'; --vscode-icon-play-font-family: 'codicon'; --vscode-icon-run-content: '\eb2c'; --vscode-icon-run-font-family: 'codicon'; --vscode-icon-plug-content: '\eb2d'; --vscode-icon-plug-font-family: 'codicon'; --vscode-icon-preserve-case-content: '\eb2e'; --vscode-icon-preserve-case-font-family: 'codicon'; --vscode-icon-preview-content: '\eb2f'; --vscode-icon-preview-font-family: 'codicon'; --vscode-icon-project-content: '\eb30'; --vscode-icon-project-font-family: 'codicon'; --vscode-icon-pulse-content: '\eb31'; --vscode-icon-pulse-font-family: 'codicon'; --vscode-icon-question-content: '\eb32'; --vscode-icon-question-font-family: 'codicon'; --vscode-icon-quote-content: '\eb33'; --vscode-icon-quote-font-family: 'codicon'; --vscode-icon-radio-tower-content: '\eb34'; --vscode-icon-radio-tower-font-family: 'codicon'; --vscode-icon-reactions-content: '\eb35'; --vscode-icon-reactions-font-family: 'codicon'; --vscode-icon-references-content: '\eb36'; --vscode-icon-references-font-family: 'codicon'; --vscode-icon-refresh-content: '\eb37'; --vscode-icon-refresh-font-family: 'codicon'; --vscode-icon-regex-content: '\eb38'; --vscode-icon-regex-font-family: 'codicon'; --vscode-icon-remote-explorer-content: '\eb39'; --vscode-icon-remote-explorer-font-family: 'codicon'; --vscode-icon-remote-content: '\eb3a'; --vscode-icon-remote-font-family: 'codicon'; --vscode-icon-remove-content: '\eb3b'; --vscode-icon-remove-font-family: 'codicon'; --vscode-icon-replace-all-content: '\eb3c'; --vscode-icon-replace-all-font-family: 'codicon'; --vscode-icon-replace-content: '\eb3d'; --vscode-icon-replace-font-family: 'codicon'; --vscode-icon-repo-clone-content: '\eb3e'; --vscode-icon-repo-clone-font-family: 'codicon'; --vscode-icon-repo-force-push-content: '\eb3f'; --vscode-icon-repo-force-push-font-family: 'codicon'; --vscode-icon-repo-pull-content: '\eb40'; --vscode-icon-repo-pull-font-family: 'codicon'; --vscode-icon-repo-push-content: '\eb41'; --vscode-icon-repo-push-font-family: 'codicon'; --vscode-icon-report-content: '\eb42'; --vscode-icon-report-font-family: 'codicon'; --vscode-icon-request-changes-content: '\eb43'; --vscode-icon-request-changes-font-family: 'codicon'; --vscode-icon-rocket-content: '\eb44'; --vscode-icon-rocket-font-family: 'codicon'; --vscode-icon-root-folder-opened-content: '\eb45'; --vscode-icon-root-folder-opened-font-family: 'codicon'; --vscode-icon-root-folder-content: '\eb46'; --vscode-icon-root-folder-font-family: 'codicon'; --vscode-icon-rss-content: '\eb47'; --vscode-icon-rss-font-family: 'codicon'; --vscode-icon-ruby-content: '\eb48'; --vscode-icon-ruby-font-family: 'codicon'; --vscode-icon-save-all-content: '\eb49'; --vscode-icon-save-all-font-family: 'codicon'; --vscode-icon-save-as-content: '\eb4a'; --vscode-icon-save-as-font-family: 'codicon'; --vscode-icon-save-content: '\eb4b'; --vscode-icon-save-font-family: 'codicon'; --vscode-icon-screen-full-content: '\eb4c'; --vscode-icon-screen-full-font-family: 'codicon'; --vscode-icon-screen-normal-content: '\eb4d'; --vscode-icon-screen-normal-font-family: 'codicon'; --vscode-icon-search-stop-content: '\eb4e'; --vscode-icon-search-stop-font-family: 'codicon'; --vscode-icon-server-content: '\eb50'; --vscode-icon-server-font-family: 'codicon'; --vscode-icon-settings-gear-content: '\eb51'; --vscode-icon-settings-gear-font-family: 'codicon'; --vscode-icon-settings-content: '\eb52'; --vscode-icon-settings-font-family: 'codicon'; --vscode-icon-shield-content: '\eb53'; --vscode-icon-shield-font-family: 'codicon'; --vscode-icon-smiley-content: '\eb54'; --vscode-icon-smiley-font-family: 'codicon'; --vscode-icon-sort-precedence-content: '\eb55'; --vscode-icon-sort-precedence-font-family: 'codicon'; --vscode-icon-split-horizontal-content: '\eb56'; --vscode-icon-split-horizontal-font-family: 'codicon'; --vscode-icon-split-vertical-content: '\eb57'; --vscode-icon-split-vertical-font-family: 'codicon'; --vscode-icon-squirrel-content: '\eb58'; --vscode-icon-squirrel-font-family: 'codicon'; --vscode-icon-star-full-content: '\eb59'; --vscode-icon-star-full-font-family: 'codicon'; --vscode-icon-star-half-content: '\eb5a'; --vscode-icon-star-half-font-family: 'codicon'; --vscode-icon-symbol-class-content: '\eb5b'; --vscode-icon-symbol-class-font-family: 'codicon'; --vscode-icon-symbol-color-content: '\eb5c'; --vscode-icon-symbol-color-font-family: 'codicon'; --vscode-icon-symbol-constant-content: '\eb5d'; --vscode-icon-symbol-constant-font-family: 'codicon'; --vscode-icon-symbol-enum-member-content: '\eb5e'; --vscode-icon-symbol-enum-member-font-family: 'codicon'; --vscode-icon-symbol-field-content: '\eb5f'; --vscode-icon-symbol-field-font-family: 'codicon'; --vscode-icon-symbol-file-content: '\eb60'; --vscode-icon-symbol-file-font-family: 'codicon'; --vscode-icon-symbol-interface-content: '\eb61'; --vscode-icon-symbol-interface-font-family: 'codicon'; --vscode-icon-symbol-keyword-content: '\eb62'; --vscode-icon-symbol-keyword-font-family: 'codicon'; --vscode-icon-symbol-misc-content: '\eb63'; --vscode-icon-symbol-misc-font-family: 'codicon'; --vscode-icon-symbol-operator-content: '\eb64'; --vscode-icon-symbol-operator-font-family: 'codicon'; --vscode-icon-symbol-property-content: '\eb65'; --vscode-icon-symbol-property-font-family: 'codicon'; --vscode-icon-wrench-content: '\eb65'; --vscode-icon-wrench-font-family: 'codicon'; --vscode-icon-wrench-subaction-content: '\eb65'; --vscode-icon-wrench-subaction-font-family: 'codicon'; --vscode-icon-symbol-snippet-content: '\eb66'; --vscode-icon-symbol-snippet-font-family: 'codicon'; --vscode-icon-tasklist-content: '\eb67'; --vscode-icon-tasklist-font-family: 'codicon'; --vscode-icon-telescope-content: '\eb68'; --vscode-icon-telescope-font-family: 'codicon'; --vscode-icon-text-size-content: '\eb69'; --vscode-icon-text-size-font-family: 'codicon'; --vscode-icon-three-bars-content: '\eb6a'; --vscode-icon-three-bars-font-family: 'codicon'; --vscode-icon-thumbsdown-content: '\eb6b'; --vscode-icon-thumbsdown-font-family: 'codicon'; --vscode-icon-thumbsup-content: '\eb6c'; --vscode-icon-thumbsup-font-family: 'codicon'; --vscode-icon-tools-content: '\eb6d'; --vscode-icon-tools-font-family: 'codicon'; --vscode-icon-triangle-down-content: '\eb6e'; --vscode-icon-triangle-down-font-family: 'codicon'; --vscode-icon-triangle-left-content: '\eb6f'; --vscode-icon-triangle-left-font-family: 'codicon'; --vscode-icon-triangle-right-content: '\eb70'; --vscode-icon-triangle-right-font-family: 'codicon'; --vscode-icon-triangle-up-content: '\eb71'; --vscode-icon-triangle-up-font-family: 'codicon'; --vscode-icon-twitter-content: '\eb72'; --vscode-icon-twitter-font-family: 'codicon'; --vscode-icon-unfold-content: '\eb73'; --vscode-icon-unfold-font-family: 'codicon'; --vscode-icon-unlock-content: '\eb74'; --vscode-icon-unlock-font-family: 'codicon'; --vscode-icon-unmute-content: '\eb75'; --vscode-icon-unmute-font-family: 'codicon'; --vscode-icon-unverified-content: '\eb76'; --vscode-icon-unverified-font-family: 'codicon'; --vscode-icon-verified-content: '\eb77'; --vscode-icon-verified-font-family: 'codicon'; --vscode-icon-versions-content: '\eb78'; --vscode-icon-versions-font-family: 'codicon'; --vscode-icon-vm-active-content: '\eb79'; --vscode-icon-vm-active-font-family: 'codicon'; --vscode-icon-vm-outline-content: '\eb7a'; --vscode-icon-vm-outline-font-family: 'codicon'; --vscode-icon-vm-running-content: '\eb7b'; --vscode-icon-vm-running-font-family: 'codicon'; --vscode-icon-watch-content: '\eb7c'; --vscode-icon-watch-font-family: 'codicon'; --vscode-icon-whitespace-content: '\eb7d'; --vscode-icon-whitespace-font-family: 'codicon'; --vscode-icon-whole-word-content: '\eb7e'; --vscode-icon-whole-word-font-family: 'codicon'; --vscode-icon-window-content: '\eb7f'; --vscode-icon-window-font-family: 'codicon'; --vscode-icon-word-wrap-content: '\eb80'; --vscode-icon-word-wrap-font-family: 'codicon'; --vscode-icon-zoom-in-content: '\eb81'; --vscode-icon-zoom-in-font-family: 'codicon'; --vscode-icon-zoom-out-content: '\eb82'; --vscode-icon-zoom-out-font-family: 'codicon'; --vscode-icon-list-filter-content: '\eb83'; --vscode-icon-list-filter-font-family: 'codicon'; --vscode-icon-list-flat-content: '\eb84'; --vscode-icon-list-flat-font-family: 'codicon'; --vscode-icon-list-selection-content: '\eb85'; --vscode-icon-list-selection-font-family: 'codicon'; --vscode-icon-selection-content: '\eb85'; --vscode-icon-selection-font-family: 'codicon'; --vscode-icon-list-tree-content: '\eb86'; --vscode-icon-list-tree-font-family: 'codicon'; --vscode-icon-debug-breakpoint-function-unverified-content: '\eb87'; --vscode-icon-debug-breakpoint-function-unverified-font-family: 'codicon'; --vscode-icon-debug-breakpoint-function-content: '\eb88'; --vscode-icon-debug-breakpoint-function-font-family: 'codicon'; --vscode-icon-debug-breakpoint-function-disabled-content: '\eb88'; --vscode-icon-debug-breakpoint-function-disabled-font-family: 'codicon'; --vscode-icon-debug-stackframe-active-content: '\eb89'; --vscode-icon-debug-stackframe-active-font-family: 'codicon'; --vscode-icon-circle-small-filled-content: '\eb8a'; --vscode-icon-circle-small-filled-font-family: 'codicon'; --vscode-icon-debug-stackframe-dot-content: '\eb8a'; --vscode-icon-debug-stackframe-dot-font-family: 'codicon'; --vscode-icon-terminal-decoration-mark-content: '\eb8a'; --vscode-icon-terminal-decoration-mark-font-family: 'codicon'; --vscode-icon-debug-stackframe-content: '\eb8b'; --vscode-icon-debug-stackframe-font-family: 'codicon'; --vscode-icon-debug-stackframe-focused-content: '\eb8b'; --vscode-icon-debug-stackframe-focused-font-family: 'codicon'; --vscode-icon-debug-breakpoint-unsupported-content: '\eb8c'; --vscode-icon-debug-breakpoint-unsupported-font-family: 'codicon'; --vscode-icon-symbol-string-content: '\eb8d'; --vscode-icon-symbol-string-font-family: 'codicon'; --vscode-icon-debug-reverse-continue-content: '\eb8e'; --vscode-icon-debug-reverse-continue-font-family: 'codicon'; --vscode-icon-debug-step-back-content: '\eb8f'; --vscode-icon-debug-step-back-font-family: 'codicon'; --vscode-icon-debug-restart-frame-content: '\eb90'; --vscode-icon-debug-restart-frame-font-family: 'codicon'; --vscode-icon-debug-alt-content: '\eb91'; --vscode-icon-debug-alt-font-family: 'codicon'; --vscode-icon-call-incoming-content: '\eb92'; --vscode-icon-call-incoming-font-family: 'codicon'; --vscode-icon-call-outgoing-content: '\eb93'; --vscode-icon-call-outgoing-font-family: 'codicon'; --vscode-icon-menu-content: '\eb94'; --vscode-icon-menu-font-family: 'codicon'; --vscode-icon-expand-all-content: '\eb95'; --vscode-icon-expand-all-font-family: 'codicon'; --vscode-icon-feedback-content: '\eb96'; --vscode-icon-feedback-font-family: 'codicon'; --vscode-icon-git-pull-request-reviewer-content: '\eb96'; --vscode-icon-git-pull-request-reviewer-font-family: 'codicon'; --vscode-icon-group-by-ref-type-content: '\eb97'; --vscode-icon-group-by-ref-type-font-family: 'codicon'; --vscode-icon-ungroup-by-ref-type-content: '\eb98'; --vscode-icon-ungroup-by-ref-type-font-family: 'codicon'; --vscode-icon-account-content: '\eb99'; --vscode-icon-account-font-family: 'codicon'; --vscode-icon-git-pull-request-assignee-content: '\eb99'; --vscode-icon-git-pull-request-assignee-font-family: 'codicon'; --vscode-icon-bell-dot-content: '\eb9a'; --vscode-icon-bell-dot-font-family: 'codicon'; --vscode-icon-debug-console-content: '\eb9b'; --vscode-icon-debug-console-font-family: 'codicon'; --vscode-icon-library-content: '\eb9c'; --vscode-icon-library-font-family: 'codicon'; --vscode-icon-output-content: '\eb9d'; --vscode-icon-output-font-family: 'codicon'; --vscode-icon-run-all-content: '\eb9e'; --vscode-icon-run-all-font-family: 'codicon'; --vscode-icon-sync-ignored-content: '\eb9f'; --vscode-icon-sync-ignored-font-family: 'codicon'; --vscode-icon-pinned-content: '\eba0'; --vscode-icon-pinned-font-family: 'codicon'; --vscode-icon-github-inverted-content: '\eba1'; --vscode-icon-github-inverted-font-family: 'codicon'; --vscode-icon-server-process-content: '\eba2'; --vscode-icon-server-process-font-family: 'codicon'; --vscode-icon-server-environment-content: '\eba3'; --vscode-icon-server-environment-font-family: 'codicon'; --vscode-icon-pass-content: '\eba4'; --vscode-icon-pass-font-family: 'codicon'; --vscode-icon-issue-closed-content: '\eba4'; --vscode-icon-issue-closed-font-family: 'codicon'; --vscode-icon-stop-circle-content: '\eba5'; --vscode-icon-stop-circle-font-family: 'codicon'; --vscode-icon-play-circle-content: '\eba6'; --vscode-icon-play-circle-font-family: 'codicon'; --vscode-icon-record-content: '\eba7'; --vscode-icon-record-font-family: 'codicon'; --vscode-icon-debug-alt-small-content: '\eba8'; --vscode-icon-debug-alt-small-font-family: 'codicon'; --vscode-icon-vm-connect-content: '\eba9'; --vscode-icon-vm-connect-font-family: 'codicon'; --vscode-icon-cloud-content: '\ebaa'; --vscode-icon-cloud-font-family: 'codicon'; --vscode-icon-merge-content: '\ebab'; --vscode-icon-merge-font-family: 'codicon'; --vscode-icon-export-content: '\ebac'; --vscode-icon-export-font-family: 'codicon'; --vscode-icon-graph-left-content: '\ebad'; --vscode-icon-graph-left-font-family: 'codicon'; --vscode-icon-magnet-content: '\ebae'; --vscode-icon-magnet-font-family: 'codicon'; --vscode-icon-notebook-content: '\ebaf'; --vscode-icon-notebook-font-family: 'codicon'; --vscode-icon-redo-content: '\ebb0'; --vscode-icon-redo-font-family: 'codicon'; --vscode-icon-check-all-content: '\ebb1'; --vscode-icon-check-all-font-family: 'codicon'; --vscode-icon-pinned-dirty-content: '\ebb2'; --vscode-icon-pinned-dirty-font-family: 'codicon'; --vscode-icon-pass-filled-content: '\ebb3'; --vscode-icon-pass-filled-font-family: 'codicon'; --vscode-icon-circle-large-filled-content: '\ebb4'; --vscode-icon-circle-large-filled-font-family: 'codicon'; --vscode-icon-circle-large-content: '\ebb5'; --vscode-icon-circle-large-font-family: 'codicon'; --vscode-icon-circle-large-outline-content: '\ebb5'; --vscode-icon-circle-large-outline-font-family: 'codicon'; --vscode-icon-combine-content: '\ebb6'; --vscode-icon-combine-font-family: 'codicon'; --vscode-icon-gather-content: '\ebb6'; --vscode-icon-gather-font-family: 'codicon'; --vscode-icon-table-content: '\ebb7'; --vscode-icon-table-font-family: 'codicon'; --vscode-icon-variable-group-content: '\ebb8'; --vscode-icon-variable-group-font-family: 'codicon'; --vscode-icon-type-hierarchy-content: '\ebb9'; --vscode-icon-type-hierarchy-font-family: 'codicon'; --vscode-icon-type-hierarchy-sub-content: '\ebba'; --vscode-icon-type-hierarchy-sub-font-family: 'codicon'; --vscode-icon-type-hierarchy-super-content: '\ebbb'; --vscode-icon-type-hierarchy-super-font-family: 'codicon'; --vscode-icon-git-pull-request-create-content: '\ebbc'; --vscode-icon-git-pull-request-create-font-family: 'codicon'; --vscode-icon-run-above-content: '\ebbd'; --vscode-icon-run-above-font-family: 'codicon'; --vscode-icon-run-below-content: '\ebbe'; --vscode-icon-run-below-font-family: 'codicon'; --vscode-icon-notebook-template-content: '\ebbf'; --vscode-icon-notebook-template-font-family: 'codicon'; --vscode-icon-debug-rerun-content: '\ebc0'; --vscode-icon-debug-rerun-font-family: 'codicon'; --vscode-icon-workspace-trusted-content: '\ebc1'; --vscode-icon-workspace-trusted-font-family: 'codicon'; --vscode-icon-workspace-untrusted-content: '\ebc2'; --vscode-icon-workspace-untrusted-font-family: 'codicon'; --vscode-icon-workspace-unknown-content: '\ebc3'; --vscode-icon-workspace-unknown-font-family: 'codicon'; --vscode-icon-terminal-cmd-content: '\ebc4'; --vscode-icon-terminal-cmd-font-family: 'codicon'; --vscode-icon-terminal-debian-content: '\ebc5'; --vscode-icon-terminal-debian-font-family: 'codicon'; --vscode-icon-terminal-linux-content: '\ebc6'; --vscode-icon-terminal-linux-font-family: 'codicon'; --vscode-icon-terminal-powershell-content: '\ebc7'; --vscode-icon-terminal-powershell-font-family: 'codicon'; --vscode-icon-terminal-tmux-content: '\ebc8'; --vscode-icon-terminal-tmux-font-family: 'codicon'; --vscode-icon-terminal-ubuntu-content: '\ebc9'; --vscode-icon-terminal-ubuntu-font-family: 'codicon'; --vscode-icon-terminal-bash-content: '\ebca'; --vscode-icon-terminal-bash-font-family: 'codicon'; --vscode-icon-arrow-swap-content: '\ebcb'; --vscode-icon-arrow-swap-font-family: 'codicon'; --vscode-icon-copy-content: '\ebcc'; --vscode-icon-copy-font-family: 'codicon'; --vscode-icon-person-add-content: '\ebcd'; --vscode-icon-person-add-font-family: 'codicon'; --vscode-icon-filter-filled-content: '\ebce'; --vscode-icon-filter-filled-font-family: 'codicon'; --vscode-icon-wand-content: '\ebcf'; --vscode-icon-wand-font-family: 'codicon'; --vscode-icon-debug-line-by-line-content: '\ebd0'; --vscode-icon-debug-line-by-line-font-family: 'codicon'; --vscode-icon-inspect-content: '\ebd1'; --vscode-icon-inspect-font-family: 'codicon'; --vscode-icon-layers-content: '\ebd2'; --vscode-icon-layers-font-family: 'codicon'; --vscode-icon-layers-dot-content: '\ebd3'; --vscode-icon-layers-dot-font-family: 'codicon'; --vscode-icon-layers-active-content: '\ebd4'; --vscode-icon-layers-active-font-family: 'codicon'; --vscode-icon-compass-content: '\ebd5'; --vscode-icon-compass-font-family: 'codicon'; --vscode-icon-compass-dot-content: '\ebd6'; --vscode-icon-compass-dot-font-family: 'codicon'; --vscode-icon-compass-active-content: '\ebd7'; --vscode-icon-compass-active-font-family: 'codicon'; --vscode-icon-azure-content: '\ebd8'; --vscode-icon-azure-font-family: 'codicon'; --vscode-icon-issue-draft-content: '\ebd9'; --vscode-icon-issue-draft-font-family: 'codicon'; --vscode-icon-git-pull-request-closed-content: '\ebda'; --vscode-icon-git-pull-request-closed-font-family: 'codicon'; --vscode-icon-git-pull-request-draft-content: '\ebdb'; --vscode-icon-git-pull-request-draft-font-family: 'codicon'; --vscode-icon-debug-all-content: '\ebdc'; --vscode-icon-debug-all-font-family: 'codicon'; --vscode-icon-debug-coverage-content: '\ebdd'; --vscode-icon-debug-coverage-font-family: 'codicon'; --vscode-icon-run-errors-content: '\ebde'; --vscode-icon-run-errors-font-family: 'codicon'; --vscode-icon-folder-library-content: '\ebdf'; --vscode-icon-folder-library-font-family: 'codicon'; --vscode-icon-debug-continue-small-content: '\ebe0'; --vscode-icon-debug-continue-small-font-family: 'codicon'; --vscode-icon-beaker-stop-content: '\ebe1'; --vscode-icon-beaker-stop-font-family: 'codicon'; --vscode-icon-graph-line-content: '\ebe2'; --vscode-icon-graph-line-font-family: 'codicon'; --vscode-icon-graph-scatter-content: '\ebe3'; --vscode-icon-graph-scatter-font-family: 'codicon'; --vscode-icon-pie-chart-content: '\ebe4'; --vscode-icon-pie-chart-font-family: 'codicon'; --vscode-icon-bracket-content: '\eb0f'; --vscode-icon-bracket-font-family: 'codicon'; --vscode-icon-bracket-dot-content: '\ebe5'; --vscode-icon-bracket-dot-font-family: 'codicon'; --vscode-icon-bracket-error-content: '\ebe6'; --vscode-icon-bracket-error-font-family: 'codicon'; --vscode-icon-lock-small-content: '\ebe7'; --vscode-icon-lock-small-font-family: 'codicon'; --vscode-icon-azure-devops-content: '\ebe8'; --vscode-icon-azure-devops-font-family: 'codicon'; --vscode-icon-verified-filled-content: '\ebe9'; --vscode-icon-verified-filled-font-family: 'codicon'; --vscode-icon-newline-content: '\ebea'; --vscode-icon-newline-font-family: 'codicon'; --vscode-icon-layout-content: '\ebeb'; --vscode-icon-layout-font-family: 'codicon'; --vscode-icon-layout-activitybar-left-content: '\ebec'; --vscode-icon-layout-activitybar-left-font-family: 'codicon'; --vscode-icon-layout-activitybar-right-content: '\ebed'; --vscode-icon-layout-activitybar-right-font-family: 'codicon'; --vscode-icon-layout-panel-left-content: '\ebee'; --vscode-icon-layout-panel-left-font-family: 'codicon'; --vscode-icon-layout-panel-center-content: '\ebef'; --vscode-icon-layout-panel-center-font-family: 'codicon'; --vscode-icon-layout-panel-justify-content: '\ebf0'; --vscode-icon-layout-panel-justify-font-family: 'codicon'; --vscode-icon-layout-panel-right-content: '\ebf1'; --vscode-icon-layout-panel-right-font-family: 'codicon'; --vscode-icon-layout-panel-content: '\ebf2'; --vscode-icon-layout-panel-font-family: 'codicon'; --vscode-icon-layout-sidebar-left-content: '\ebf3'; --vscode-icon-layout-sidebar-left-font-family: 'codicon'; --vscode-icon-layout-sidebar-right-content: '\ebf4'; --vscode-icon-layout-sidebar-right-font-family: 'codicon'; --vscode-icon-layout-statusbar-content: '\ebf5'; --vscode-icon-layout-statusbar-font-family: 'codicon'; --vscode-icon-layout-menubar-content: '\ebf6'; --vscode-icon-layout-menubar-font-family: 'codicon'; --vscode-icon-layout-centered-content: '\ebf7'; --vscode-icon-layout-centered-font-family: 'codicon'; --vscode-icon-target-content: '\ebf8'; --vscode-icon-target-font-family: 'codicon'; --vscode-icon-indent-content: '\ebf9'; --vscode-icon-indent-font-family: 'codicon'; --vscode-icon-record-small-content: '\ebfa'; --vscode-icon-record-small-font-family: 'codicon'; --vscode-icon-error-small-content: '\ebfb'; --vscode-icon-error-small-font-family: 'codicon'; --vscode-icon-terminal-decoration-error-content: '\ebfb'; --vscode-icon-terminal-decoration-error-font-family: 'codicon'; --vscode-icon-arrow-circle-down-content: '\ebfc'; --vscode-icon-arrow-circle-down-font-family: 'codicon'; --vscode-icon-arrow-circle-left-content: '\ebfd'; --vscode-icon-arrow-circle-left-font-family: 'codicon'; --vscode-icon-arrow-circle-right-content: '\ebfe'; --vscode-icon-arrow-circle-right-font-family: 'codicon'; --vscode-icon-arrow-circle-up-content: '\ebff'; --vscode-icon-arrow-circle-up-font-family: 'codicon'; --vscode-icon-layout-sidebar-right-off-content: '\ec00'; --vscode-icon-layout-sidebar-right-off-font-family: 'codicon'; --vscode-icon-layout-panel-off-content: '\ec01'; --vscode-icon-layout-panel-off-font-family: 'codicon'; --vscode-icon-layout-sidebar-left-off-content: '\ec02'; --vscode-icon-layout-sidebar-left-off-font-family: 'codicon'; --vscode-icon-blank-content: '\ec03'; --vscode-icon-blank-font-family: 'codicon'; --vscode-icon-heart-filled-content: '\ec04'; --vscode-icon-heart-filled-font-family: 'codicon'; --vscode-icon-map-content: '\ec05'; --vscode-icon-map-font-family: 'codicon'; --vscode-icon-map-horizontal-content: '\ec05'; --vscode-icon-map-horizontal-font-family: 'codicon'; --vscode-icon-fold-horizontal-content: '\ec05'; --vscode-icon-fold-horizontal-font-family: 'codicon'; --vscode-icon-map-filled-content: '\ec06'; --vscode-icon-map-filled-font-family: 'codicon'; --vscode-icon-map-horizontal-filled-content: '\ec06'; --vscode-icon-map-horizontal-filled-font-family: 'codicon'; --vscode-icon-fold-horizontal-filled-content: '\ec06'; --vscode-icon-fold-horizontal-filled-font-family: 'codicon'; --vscode-icon-circle-small-content: '\ec07'; --vscode-icon-circle-small-font-family: 'codicon'; --vscode-icon-bell-slash-content: '\ec08'; --vscode-icon-bell-slash-font-family: 'codicon'; --vscode-icon-bell-slash-dot-content: '\ec09'; --vscode-icon-bell-slash-dot-font-family: 'codicon'; --vscode-icon-comment-unresolved-content: '\ec0a'; --vscode-icon-comment-unresolved-font-family: 'codicon'; --vscode-icon-git-pull-request-go-to-changes-content: '\ec0b'; --vscode-icon-git-pull-request-go-to-changes-font-family: 'codicon'; --vscode-icon-git-pull-request-new-changes-content: '\ec0c'; --vscode-icon-git-pull-request-new-changes-font-family: 'codicon'; --vscode-icon-search-fuzzy-content: '\ec0d'; --vscode-icon-search-fuzzy-font-family: 'codicon'; --vscode-icon-comment-draft-content: '\ec0e'; --vscode-icon-comment-draft-font-family: 'codicon'; --vscode-icon-send-content: '\ec0f'; --vscode-icon-send-font-family: 'codicon'; --vscode-icon-sparkle-content: '\ec10'; --vscode-icon-sparkle-font-family: 'codicon'; --vscode-icon-insert-content: '\ec11'; --vscode-icon-insert-font-family: 'codicon'; --vscode-icon-mic-content: '\ec12'; --vscode-icon-mic-font-family: 'codicon'; --vscode-icon-thumbsdown-filled-content: '\ec13'; --vscode-icon-thumbsdown-filled-font-family: 'codicon'; --vscode-icon-thumbsup-filled-content: '\ec14'; --vscode-icon-thumbsup-filled-font-family: 'codicon'; --vscode-icon-coffee-content: '\ec15'; --vscode-icon-coffee-font-family: 'codicon'; --vscode-icon-snake-content: '\ec16'; --vscode-icon-snake-font-family: 'codicon'; --vscode-icon-game-content: '\ec17'; --vscode-icon-game-font-family: 'codicon'; --vscode-icon-vr-content: '\ec18'; --vscode-icon-vr-font-family: 'codicon'; --vscode-icon-chip-content: '\ec19'; --vscode-icon-chip-font-family: 'codicon'; --vscode-icon-piano-content: '\ec1a'; --vscode-icon-piano-font-family: 'codicon'; --vscode-icon-music-content: '\ec1b'; --vscode-icon-music-font-family: 'codicon'; --vscode-icon-mic-filled-content: '\ec1c'; --vscode-icon-mic-filled-font-family: 'codicon'; --vscode-icon-repo-fetch-content: '\ec1d'; --vscode-icon-repo-fetch-font-family: 'codicon'; --vscode-icon-copilot-content: '\ec1e'; --vscode-icon-copilot-font-family: 'codicon'; --vscode-icon-lightbulb-sparkle-content: '\ec1f'; --vscode-icon-lightbulb-sparkle-font-family: 'codicon'; --vscode-icon-robot-content: '\ec20'; --vscode-icon-robot-font-family: 'codicon'; --vscode-icon-sparkle-filled-content: '\ec21'; --vscode-icon-sparkle-filled-font-family: 'codicon'; --vscode-icon-diff-single-content: '\ec22'; --vscode-icon-diff-single-font-family: 'codicon'; --vscode-icon-diff-multiple-content: '\ec23'; --vscode-icon-diff-multiple-font-family: 'codicon'; --vscode-icon-surround-with-content: '\ec24'; --vscode-icon-surround-with-font-family: 'codicon'; --vscode-icon-share-content: '\ec25'; --vscode-icon-share-font-family: 'codicon'; --vscode-icon-git-stash-content: '\ec26'; --vscode-icon-git-stash-font-family: 'codicon'; --vscode-icon-git-stash-apply-content: '\ec27'; --vscode-icon-git-stash-apply-font-family: 'codicon'; --vscode-icon-git-stash-pop-content: '\ec28'; --vscode-icon-git-stash-pop-font-family: 'codicon'; --vscode-icon-vscode-content: '\ec29'; --vscode-icon-vscode-font-family: 'codicon'; --vscode-icon-vscode-insiders-content: '\ec2a'; --vscode-icon-vscode-insiders-font-family: 'codicon'; --vscode-icon-code-oss-content: '\ec2b'; --vscode-icon-code-oss-font-family: 'codicon'; --vscode-icon-run-coverage-content: '\ec2c'; --vscode-icon-run-coverage-font-family: 'codicon'; --vscode-icon-run-all-coverage-content: '\ec2d'; --vscode-icon-run-all-coverage-font-family: 'codicon'; --vscode-icon-coverage-content: '\ec2e'; --vscode-icon-coverage-font-family: 'codicon'; --vscode-icon-github-project-content: '\ec2f'; --vscode-icon-github-project-font-family: 'codicon'; --vscode-icon-map-vertical-content: '\ec30'; --vscode-icon-map-vertical-font-family: 'codicon'; --vscode-icon-fold-vertical-content: '\ec30'; --vscode-icon-fold-vertical-font-family: 'codicon'; --vscode-icon-map-vertical-filled-content: '\ec31'; --vscode-icon-map-vertical-filled-font-family: 'codicon'; --vscode-icon-fold-vertical-filled-content: '\ec31'; --vscode-icon-fold-vertical-filled-font-family: 'codicon'; --vscode-icon-go-to-search-content: '\ec32'; --vscode-icon-go-to-search-font-family: 'codicon'; --vscode-icon-percentage-content: '\ec33'; --vscode-icon-percentage-font-family: 'codicon'; --vscode-icon-sort-percentage-content: '\ec33'; --vscode-icon-sort-percentage-font-family: 'codicon'; --vscode-icon-attach-content: '\ec34'; --vscode-icon-attach-font-family: 'codicon'; --vscode-icon-dialog-error-content: '\ea87'; --vscode-icon-dialog-error-font-family: 'codicon'; --vscode-icon-dialog-warning-content: '\ea6c'; --vscode-icon-dialog-warning-font-family: 'codicon'; --vscode-icon-dialog-info-content: '\ea74'; --vscode-icon-dialog-info-font-family: 'codicon'; --vscode-icon-dialog-close-content: '\ea76'; --vscode-icon-dialog-close-font-family: 'codicon'; --vscode-icon-tree-item-expanded-content: '\eab4'; --vscode-icon-tree-item-expanded-font-family: 'codicon'; --vscode-icon-tree-filter-on-type-on-content: '\eb83'; --vscode-icon-tree-filter-on-type-on-font-family: 'codicon'; --vscode-icon-tree-filter-on-type-off-content: '\eb85'; --vscode-icon-tree-filter-on-type-off-font-family: 'codicon'; --vscode-icon-tree-filter-clear-content: '\ea76'; --vscode-icon-tree-filter-clear-font-family: 'codicon'; --vscode-icon-tree-item-loading-content: '\eb19'; --vscode-icon-tree-item-loading-font-family: 'codicon'; --vscode-icon-menu-selection-content: '\eab2'; --vscode-icon-menu-selection-font-family: 'codicon'; --vscode-icon-menu-submenu-content: '\eab6'; --vscode-icon-menu-submenu-font-family: 'codicon'; --vscode-icon-menubar-more-content: '\ea7c'; --vscode-icon-menubar-more-font-family: 'codicon'; --vscode-icon-scrollbar-button-left-content: '\eb6f'; --vscode-icon-scrollbar-button-left-font-family: 'codicon'; --vscode-icon-scrollbar-button-right-content: '\eb70'; --vscode-icon-scrollbar-button-right-font-family: 'codicon'; --vscode-icon-scrollbar-button-up-content: '\eb71'; --vscode-icon-scrollbar-button-up-font-family: 'codicon'; --vscode-icon-scrollbar-button-down-content: '\eb6e'; --vscode-icon-scrollbar-button-down-font-family: 'codicon'; --vscode-icon-toolbar-more-content: '\ea7c'; --vscode-icon-toolbar-more-font-family: 'codicon'; --vscode-icon-quick-input-back-content: '\ea9b'; --vscode-icon-quick-input-back-font-family: 'codicon'; --vscode-icon-drop-down-button-content: '\eab4'; --vscode-icon-drop-down-button-font-family: 'codicon'; --vscode-icon-symbol-customcolor-content: '\eb5c'; --vscode-icon-symbol-customcolor-font-family: 'codicon'; --vscode-icon-workspace-unspecified-content: '\ebc3'; --vscode-icon-workspace-unspecified-font-family: 'codicon'; --vscode-icon-git-fetch-content: '\ec1d'; --vscode-icon-git-fetch-font-family: 'codicon'; --vscode-icon-lightbulb-sparkle-autofix-content: '\ec1f'; --vscode-icon-lightbulb-sparkle-autofix-font-family: 'codicon'; --vscode-icon-debug-breakpoint-pending-content: '\ebd9'; --vscode-icon-debug-breakpoint-pending-font-family: 'codicon'; --vscode-icon-widget-close-content: '\ea76'; --vscode-icon-widget-close-font-family: 'codicon'; --vscode-icon-goto-previous-location-content: '\eaa1'; --vscode-icon-goto-previous-location-font-family: 'codicon'; --vscode-icon-goto-next-location-content: '\ea9a'; --vscode-icon-goto-next-location-font-family: 'codicon'; --vscode-icon-diff-insert-content: '\ea60'; --vscode-icon-diff-insert-font-family: 'codicon'; --vscode-icon-diff-remove-content: '\eb3b'; --vscode-icon-diff-remove-font-family: 'codicon'; --vscode-icon-folding-expanded-content: '\eab4'; --vscode-icon-folding-expanded-font-family: 'codicon'; --vscode-icon-folding-collapsed-content: '\eab6'; --vscode-icon-folding-collapsed-font-family: 'codicon'; --vscode-icon-folding-manual-collapsed-content: '\eab6'; --vscode-icon-folding-manual-collapsed-font-family: 'codicon'; --vscode-icon-folding-manual-expanded-content: '\eab4'; --vscode-icon-folding-manual-expanded-font-family: 'codicon'; --vscode-icon-diff-review-insert-content: '\ea60'; --vscode-icon-diff-review-insert-font-family: 'codicon'; --vscode-icon-diff-review-remove-content: '\eb3b'; --vscode-icon-diff-review-remove-font-family: 'codicon'; --vscode-icon-diff-review-close-content: '\ea76'; --vscode-icon-diff-review-close-font-family: 'codicon'; --vscode-icon-suggest-more-info-content: '\eab6'; --vscode-icon-suggest-more-info-font-family: 'codicon'; --vscode-icon-hover-increase-verbosity-content: '\ea60'; --vscode-icon-hover-increase-verbosity-font-family: 'codicon'; --vscode-icon-hover-decrease-verbosity-content: '\eb3b'; --vscode-icon-hover-decrease-verbosity-font-family: 'codicon'; --vscode-icon-gutter-lightbulb-content: '\ea61'; --vscode-icon-gutter-lightbulb-font-family: 'codicon'; --vscode-icon-gutter-lightbulb-auto-fix-content: '\eb13'; --vscode-icon-gutter-lightbulb-auto-fix-font-family: 'codicon'; --vscode-icon-gutter-lightbulb-sparkle-content: '\ec1f'; --vscode-icon-gutter-lightbulb-sparkle-font-family: 'codicon'; --vscode-icon-gutter-lightbulb-aifix-auto-fix-content: '\ec1f'; --vscode-icon-gutter-lightbulb-aifix-auto-fix-font-family: 'codicon'; --vscode-icon-gutter-lightbulb-sparkle-filled-content: '\ec21'; --vscode-icon-gutter-lightbulb-sparkle-filled-font-family: 'codicon'; --vscode-icon-find-collapsed-content: '\eab6'; --vscode-icon-find-collapsed-font-family: 'codicon'; --vscode-icon-find-expanded-content: '\eab4'; --vscode-icon-find-expanded-font-family: 'codicon'; --vscode-icon-find-selection-content: '\eb85'; --vscode-icon-find-selection-font-family: 'codicon'; --vscode-icon-find-replace-content: '\eb3d'; --vscode-icon-find-replace-font-family: 'codicon'; --vscode-icon-find-replace-all-content: '\eb3c'; --vscode-icon-find-replace-all-font-family: 'codicon'; --vscode-icon-find-previous-match-content: '\eaa1'; --vscode-icon-find-previous-match-font-family: 'codicon'; --vscode-icon-find-next-match-content: '\ea9a'; --vscode-icon-find-next-match-font-family: 'codicon'; --vscode-icon-parameter-hints-next-content: '\eab4'; --vscode-icon-parameter-hints-next-font-family: 'codicon'; --vscode-icon-parameter-hints-previous-content: '\eab7'; --vscode-icon-parameter-hints-previous-font-family: 'codicon'; --vscode-icon-inline-suggestion-hints-next-content: '\eab6'; --vscode-icon-inline-suggestion-hints-next-font-family: 'codicon'; --vscode-icon-inline-suggestion-hints-previous-content: '\eab5'; --vscode-icon-inline-suggestion-hints-previous-font-family: 'codicon'; --vscode-icon-extensions-warning-message-content: '\ea6c'; --vscode-icon-extensions-warning-message-font-family: 'codicon'; --vscode-icon-marker-navigation-next-content: '\ea9a'; --vscode-icon-marker-navigation-next-font-family: 'codicon'; --vscode-icon-marker-navigation-previous-content: '\eaa1'; --vscode-icon-marker-navigation-previous-font-family: 'codicon'; }
.monaco-editor .inputarea.ime-input { background-color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .view-overlays .current-line-exact { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-exact-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .lines-content .core-guide-indent.lvl-0 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-1 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-2 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-3 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-4 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-5 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-6 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-7 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-8 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-9 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-10 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-11 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-12 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-13 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-14 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-15 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-16 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-17 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-18 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-19 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-20 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-21 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-22 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-23 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-24 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-25 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-26 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-27 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-28 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent.lvl-29 { --indent-color: #d3d3d3; --indent-color-active: #939393; }
.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 var(--indent-color) inset; }
.monaco-editor .lines-content .core-guide-indent.indent-active { box-shadow: 1px 0 0 0 var(--indent-color-active) inset; }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .cursors-layer .cursor-primary { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .cursors-layer .cursor-secondary { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-workbench .workbench-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-workbench .workbench-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .quickfix-edit-highlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor, .monaco-diff-editor, .monaco-component { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textPreformat-foreground: #a31515;
--vscode-textPreformat-background: rgba(0, 0, 0, 0.1);
--vscode-textBlockQuote-background: #f2f2f2;
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-sash-hoverBorder: #0090f1;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editor-background: #ffffff;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #ffffff;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorStickyScroll-shadow: #dddddd;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorInlayHint-foreground: #969696;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.1);
--vscode-editorInlayHint-typeForeground: #969696;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.1);
--vscode-editorInlayHint-parameterForeground: #969696;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.1);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-editorLightBulbAi-foreground: #ddb100;
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-diffEditor-insertedTextBackground: #aceebb;
--vscode-diffEditor-removedTextBackground: #ffcecb;
--vscode-diffEditor-insertedLineBackground: #dafbe1;
--vscode-diffEditor-removedLineBackground: #ffebe9;
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionForeground: #616161;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #ffffff;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-radio-activeForeground: #000000;
--vscode-radio-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-radio-activeBorder: #007acc;
--vscode-radio-inactiveBorder: rgba(0, 0, 0, 0.2);
--vscode-radio-inactiveHoverBackground: rgba(184, 184, 184, 0.31);
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-dropBetweenBackground: #424242;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-editorActionList-background: #f3f3f3;
--vscode-editorActionList-foreground: #616161;
--vscode-editorActionList-focusForeground: #000000;
--vscode-editorActionList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-infoHighlight: #1a85ff;
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-search-resultsInfoForeground: #616161;
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-multiDiffEditor-background: #ffffff;
--vscode-multiDiffEditor-border: #cccccc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorMultiCursor-primary-foreground: #000000;
--vscode-editorMultiCursor-secondary-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorIndentGuide-background: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-activeBackground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background1: #d3d3d3;
--vscode-editorIndentGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-activeBackground1: #939393;
--vscode-editorIndentGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorIndentGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #ffffff;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bf8803;
--vscode-diffEditor-move-border: rgba(139, 139, 139, 0.61);
--vscode-diffEditor-moveActive-border: #ffa500;
--vscode-diffEditor-unchangedRegionShadow: rgba(115, 115, 115, 0.75);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-foldPlaceholderForeground: #808080;
--vscode-editorGutter-foldingControlForeground: #424242;
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editor-placeholder-foreground: rgba(0, 0, 0, 0.47);
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-actionBar-toggledBackground: rgba(0, 144, 241, 0.2);
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #ffffff; }

.mtk1 { color: #000000; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #a53434; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #6a5221; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #9723b4; }
.mtk20 { color: #af00db; }
.mtk21 { color: #a31515; }
.mtk22 { color: #800000; }
.mtk23 { color: #e00000; }
.mtk24 { color: #3030c0; }
.mtk25 { color: #666666; }
.mtk26 { color: #778899; }
.mtk27 { color: #c700c7; }
.mtk28 { color: #4f76ac; }
.mtk29 { color: #008080; }
.mtk30 { color: #001188; }
.mtk31 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="enable-motion underline-links" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./train_files/gapi_loader.js.download" nonce=""></script><script src="./train_files/socketio_binary.js.download" nonce=""></script><script src="./train_files/MathJax.js.download" nonce=""></script><script src="./train_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./train_files/external_binary_es6.js.download" nonce=""></script><script nonce="">window.performance.mark('colab_load_end'); window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');</script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!---->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$739266375$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!---->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$739266375$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_Z" ng-non-bindable=""><div class="gb_2c"><div>Google Account</div><div class="gb_g">Safdar Shar</div><div>safdarshar6@gmail.com</div><div class="gb_1c"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Od;_.Md=function(a){var b=a.length;if(b>0){let c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Od=function(a){return new _.Nd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Pd=globalThis.trustedTypes;_.Qd=class{constructor(a){this.j=a}toString(){return this.j}};_.Rd=new _.Qd("about:invalid#zClosurez");_.Nd=class{constructor(a){this.Ui=a}};_.Sd=[Od("data"),Od("http"),Od("https"),Od("mailto"),Od("ftp"),new _.Nd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Td=class{constructor(a){this.j=a}toString(){return this.j+""}};_.Ud=new _.Td(_.Pd?_.Pd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
_.Vd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Qa)(a)?a|0:void 0};_.Wd=function(a,b){return a.lastIndexOf(b,0)==0};
}catch(e){_._DumpException(e)}
try{
var Yd,je,Xd,Zd,me,ee;Yd=function(){var a=null;if(!Xd)return a;try{let b=c=>c;a=Xd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.$d=function(){Zd===void 0&&(Zd=Yd());return Zd};_.be=function(a){var b=_.$d();a=b?b.createScriptURL(a):a;return new _.ae(a)};_.ce=function(a){if(a instanceof _.ae)return a.j;throw Error("x");};_.de=function(a){if(a instanceof _.Qd)return a.j;throw Error("x");};_.fe=function(a){if(ee.test(a))return a};
_.ge=function(a){return a instanceof _.Qd?_.de(a):_.fe(a)};_.he=function(a,b=document){var c,d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.R=function(a,b,c){return _.Pa(_.Nc(a,b,c,_.Mc))};_.ie=function(a,b){return _.Vd(_.Nc(a,b,void 0,_.Mc))};je=class extends _.P{constructor(a){super(a)}qc(a){return _.N(this,24,a)}};_.ke=function(){return _.C(_.id,je,1)};
_.le=function(a){var b=_.Na(a);return b=="array"||b=="object"&&typeof a.length=="number"};Xd=_.Pd;_.ae=class{constructor(a){this.j=a}toString(){return this.j+""}};ee=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var se,we,ne;_.pe=function(a){return a?new ne(_.oe(a)):me||(me=new ne)};_.qe=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.re(c,"*",a,b)[0]||null);return a||null};_.re=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.te=function(a,b){_.Cb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:se.hasOwnProperty(d)?a.setAttribute(se[d],c):_.Wd(d,"aria-")||_.Wd(d,"data-")?a.setAttribute(d,c):a[d]=c})};se={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ue=function(a){return a?a.defaultView:window};_.xe=function(a,b){var c=b[1],d=_.ve(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.te(d,c));b.length>2&&we(a,d,b);return d};we=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){let f=c[e];!_.le(f)||_.Mb(f)&&f.nodeType>0?d(f):_.dc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Md(f):f,d)}};
_.ye=function(a){return _.ve(document,a)};_.ve=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ze=function(a,b){a.appendChild(b)};_.Ae=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.Be=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.Ce=function(a,b){return a&&b?a==b||a.contains(b):!1};_.oe=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};ne=function(a){this.j=a||_.t.document||document};
_.m=ne.prototype;_.m.H=function(a){return _.qe(this.j,a)};_.m.Ta=function(a,b,c){return _.xe(this.j,arguments)};_.m.appendChild=_.ze;_.m.tf=_.Ae;_.m.Vg=_.Be;_.m.Ug=_.Ce;
}catch(e){_._DumpException(e)}
try{
_.Zi=function(a,b){a.src=_.ce(b).toString()};_.$i=function(a){var b=_.he("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.aj=function(a,b){a.src=_.ce(b);_.$i(a)};_.bj=function(a){if(!a)return null;a=_.K(a,4);var b;a===null||a===void 0?b=null:b=_.be(a);return b};_.cj=function(a,b,c){a=a.ma;return _.zb(a,a[_.v]|0,b,c)!==void 0};_.dj=class extends _.P{constructor(a){super(a)}};_.ej=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var gj=function(a,b){a<b?fj(a+1,b):_.Yc.log(Error("aa`"+a+"`"+b))},fj=function(a,b){if(hj){let c=_.ye("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";_.aj(c,hj);c.onerror=_.Pb(gj,a,b,c.src);_.ej("HEAD")[0].appendChild(c)}},ij=class extends _.P{constructor(a){super(a)}};var jj=_.C(_.id,ij,17)||new ij,kj,hj=(kj=_.C(jj,_.dj,1))?_.bj(kj):null,lj,mj=(lj=_.C(jj,_.dj,2))?_.bj(lj):null,nj=function(){fj(1,2);if(mj){let a=_.ye("LINK");a.setAttribute("type","text/css");a.href=_.ce(mj).toString();a.rel="stylesheet";let b=_.he("style",document);b&&a.setAttribute("nonce",b);_.ej("HEAD")[0].appendChild(a)}};(function(){var a=_.ke();if(_.R(a,18))nj();else{let b=_.ie(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(nj,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./train_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$739266375$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><a id="link" class="button" href="https://colab.research.google.com/drive/1Hv0koyvHCNd91Vr1bZDS3DqGwHbXr87j#notebook-main"><!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </a>
    </template><!--?lit$739266375$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$739266375$-->
    <!--?lit$739266375$-->
          <div id="private-outputs-warning" hidden="" class="header-warning private-outputs-warning"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$739266375$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1Hv0koyvHCNd91Vr1bZDS3DqGwHbXr87j#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$739266375$--> <!--?lit$739266375$-->
    <div hidden="" class="header-warning refresh-warning undismissible"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
      <div class="message"><!--?lit$739266375$-->Your Colab version is out of date, please refresh to get the latest updates.</div>
      <div class="actions">
        <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
          <!--?lit$739266375$-->Refresh to update
        </md-text-button>
      </div>
    </div>
  
    <!--?lit$739266375$-->
    <!--?lit$739266375$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div><div><div class="jimothy-path"><div class="jimothy"></div></div></div></div>
      <div id="header-content">
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><div id="header-logo">
              <colab-logo><template shadowrootmode="open"><!----><a href="https://colab.research.google.com/" aria-label="Colab home"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$--><svg viewBox="0 0 24 24"><!--?lit$739266375$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon></a></template>
              </colab-logo>
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$739266375$--><!--?lit$739266375$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" style="width: 68.0125px;" aria-describedby="doc-name-tooltip"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">train.py_</colab-input-sizer>
            <!--?lit$739266375$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$739266375$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$739266375$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$739266375$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$739266375$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$739266375$-->
      <!--?lit$739266375$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$739266375$--><md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$739266375$--><md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$739266375$--><md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->people</md-icon>
                <!--?lit$739266375$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" hidden="" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
            <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
            <!--?lit$739266375$-->Gemini
          </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ra gb_Nd gb_Jb gb_e gb_cb gb_md" id="gb" style="background-color: transparent;"><div class="gb_be gb_Fb gb_2d" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Md" style="display:block"><div class="gb_sd"></div><div class="gb_z gb_Ed gb_1f gb_8"><div class="gb_D gb_Eb gb_1f gb_8"><a class="gb_C gb_9a gb_8" aria-expanded="false" aria-label="Google Account: Safdar Shar  
(safdarshar6@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/notebook&amp;ec=GBRAqQM" tabindex="0" role="button"><span class="gb_ke"><img class="gb_X gbii" src="./train_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZygIo8mWzsdK8hNa_4_rG1KXT_GAIrOAqfalgm1-miDSbYWu=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZygIo8mWzsdK8hNa_4_rG1KXT_GAIrOAqfalgm1-miDSbYWu=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_0 gb_1" aria-hidden="true"><svg class="gb_Ua" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Va" cx="7" cy="7" r="7"></circle><path class="gb_Xa" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 424px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Cd=function(a,b,c){if(!a.v)if(c instanceof Array)for(var d of c)_.Cd(a,b,d);else{d=(0,_.z)(a.F,a,b);let e=a.B+c;a.B++;b.dataset.eqid=e;a.D[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.A.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Dd=document.querySelector(".gb_L .gb_C"),Ed=document.querySelector("#gb.gb_jd");Dd&&!Ed&&_.Cd(_.md,Dd,"click");
}catch(e){_._DumpException(e)}
try{
_.xh=function(a){if(a.B)return a.B;for(let b in a.j)if(a.j[b].Z()&&a.j[b].C())return a.j[b];return null};_.yh=function(a,b){a.j[b.K()]=b};var zh=new class extends _.x{constructor(){var a=_.Yc;super();this.D=a;this.B=null;this.A={};this.F={};this.j={};this.v=null}C(a){this.j[a]&&(_.xh(this)&&_.xh(this).K()==a||this.j[a].P(!0))}Wa(a){this.v=a;for(let b in this.j)this.j[b].Z()&&this.j[b].Wa(a)}Mb(a){return a in this.j?this.j[a]:null}};_.pd("dd",zh);
}catch(e){_._DumpException(e)}
try{
_.Si=function(a,b){return _.L(a,36,b)};_.Ti={yf:"gb_z",Ld:"gb_9a",Cl:"gb_Eb",qf:"gb_7a",zm:"gb_Df",Pm:"gb_fb",Qm:"gb_hb",Fo:"gb_db",Bh:"gb_V"};
}catch(e){_._DumpException(e)}
try{
var Ui=document.querySelector(`.${_.Ti.yf} .gb_C`),Vi=document.querySelector("#gb.gb_jd");Ui&&!Vi&&_.Cd(_.md,Ui,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$739266375$-->
    <!--?lit$739266375$--><colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <!--?lit$739266375$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$739266375$--><span class="screenreader-only"><!--?lit$739266375$-->Show command palette <!--?lit$739266375$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$739266375$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
          <!--?lit$739266375$-->Commands
        </colab-toolbar-button>
    <!--?lit$739266375$--><span class="toolbar-add-code-split"><colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code" class=" split-button "><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <!--?lit$739266375$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$739266375$--><span class="screenreader-only"><!--?lit$739266375$-->Insert code cell below <!--?lit$739266375$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$739266375$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$739266375$-->Code
            </colab-toolbar-button>
            <!--?lit$739266375$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" id="top-toolbar-add-code-dropdown-button" data-aria-label="Insert code cell options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert code cell options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="top-toolbar-add-code-dropdown-button" message="Insert code cell options"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Insert code cell options</div><!----><!--?--></template>
    </colab-tooltip-trigger></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <!--?lit$739266375$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$739266375$--><span class="screenreader-only"><!--?lit$739266375$-->Add text cell <!--?lit$739266375$--></span>
      </md-text-button>
      <!--?lit$739266375$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$739266375$-->Text
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <!--?lit$739266375$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$739266375$--><span class="screenreader-only"><!--?lit$739266375$-->Run all cells in notebook <!--?lit$739266375$--></span>
      </md-text-button>
      <!--?lit$739266375$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$739266375$-->Run all
      </colab-toolbar-button>
      <!--?lit$739266375$--><md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$739266375$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$739266375$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$739266375$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$739266375$--><!----><md-menu-item command="restart" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-menu-item command="runafter" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Run focused cell and all cells below</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$739266375$-->
    <!--?lit$739266375$-->
    <!--?lit$739266375$-->
    <!--?lit$739266375$-->
    <!--?lit$739266375$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$739266375$-->
    <!--?lit$739266375$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$739266375$--><!--?--></template></colab-connect-warning-button>
    <!--?lit$739266375$--><!--?lit$739266375$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$739266375$--> <!--?lit$739266375$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.24 GB/12.67 GB
Disk: 20.12 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <!--?lit$739266375$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$739266375$--><span class="screenreader-only"><!--?lit$739266375$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.24 GB/12.67 GB
Disk: 20.12 GB/107.72 GB <!--?lit$739266375$--></span>
      </md-text-button>
      <!--?lit$739266375$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.24 GB/12.67 GB
Disk: 20.12 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Connected to</div><!----><!----><div><!--?lit$739266375$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$739266375$-->RAM: 1.24 GB/12.67 GB</div><!----><!----><div><!--?lit$739266375$-->Disk: 20.12 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$739266375$--> <div id="connect-button-resource-display">
          <!--?lit$739266375$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$739266375$-->RAM</div>
      <!--?lit$739266375$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
          <!--?lit$739266375$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$739266375$-->Disk</div>
      <!--?lit$739266375$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        </div>
      </colab-toolbar-button>
      <!--?lit$739266375$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$739266375$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$739266375$-->
    <span class="collapsed-options">
      <!--?lit$739266375$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$739266375$-->
      <span class="colab-separator"></span>
    </span>
    <!--?lit$739266375$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" touch-target="none" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$739266375$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->code</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="show-data-inspector" data-aria-label="Data inspector" title="Data inspector" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data inspector" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->eye_tracking</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->folder</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$739266375$--><md-icon-button toggle="" command="show-data-explorer" data-aria-label="Data explorer" title="Data explorer" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data explorer" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->table</md-icon>
    </md-icon-button> <!--?lit$739266375$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$739266375$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$739266375$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-5V3AKOz7_IzN" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$739266375$--><div class="indicator"></div>
      </div>
      <!--?lit$739266375$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$739266375$--><div class="colab-tab-title">
      <!--?lit$739266375$-->
      <span id="tab-title-5V3AKOz7_IzN"><!--?lit$739266375$--><!--?lit$739266375$-->Notebook<!--?--></span>
    </div> <!--?lit$739266375$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$739266375$--><!--?--></div>
      <!--?lit$739266375$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$739266375$--><md-icon-button id="tab-pane-0-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-scroller tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$739266375$-->
              <div class="notebook-content ">
                <!--?lit$739266375$--><div class="add-cell">
      <hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell focused code-has-output" id="cell-1mhn_ewA_Iy0" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$739266375$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value="" soft-disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->arrow_upward</md-icon>
        <!--?lit$739266375$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Move cell up</div><!----><!----><div><!--?lit$739266375$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value="" soft-disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->arrow_downward</md-icon>
        <!--?lit$739266375$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Move cell down</div><!----><!----><div><!--?lit$739266375$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$739266375$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-1mhn_ewA_Iy0" anchor="ai-menu-anchor-1mhn_ewA_Iy0" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$739266375$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$739266375$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$739266375$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$739266375$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$739266375$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$739266375$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$739266375$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$739266375$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-1mhn_ewA_Iy0-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-1mhn_ewA_Iy0" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template> pen_spark </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-1mhn_ewA_Iy0" id="ai-menu-anchor-1mhn_ewA_Iy0-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->edit</md-icon>
        <!--?lit$739266375$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-set-editable-tooltip" data-aria-label="Mark cell as editable" command="set-editable" id="button-set-editable" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mark cell as editable">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->lock_open</md-icon>
        <!--?lit$739266375$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-set-editable" id="button-set-editable-tooltip" message="Mark cell as editable"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Mark cell as editable</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->delete</md-icon>
        <!--?lit$739266375$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Delete cell</div><!----><!----><div><!--?lit$739266375$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$739266375$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$739266375$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$739266375$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$739266375$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Safdar Shar
2:53 PM (0 minutes ago)
executed in 2.988s"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$739266375$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$739266375$-->executed by Safdar Shar</div><!----><!----><div><!--?lit$739266375$-->2:53 PM (0 minutes ago)</div><!----><!----><div><!--?lit$739266375$-->executed in 2.988s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$739266375$--><div class="status">
      <div class="execution-count"><!--?lit$739266375$-->[1]</div>
      <!--?lit$739266375$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->check</md-icon>
      <div><!--?lit$739266375$-->2s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 1644px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/3" style="width: 796px; height: 1644px;"><div data-mprt="3" class="overflow-guard" style="width: 796px; height: 1644px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 1644px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1644px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 1644px;"><div style="top:0px;height:19px;"></div><div style="top:19px;height:19px;"></div><div style="top:38px;height:19px;"></div><div style="top:57px;height:19px;"></div><div style="top:76px;height:19px;"></div><div style="top:95px;height:19px;"></div><div style="top:114px;height:19px;"></div><div style="top:133px;height:19px;"></div><div style="top:152px;height:19px;"></div><div style="top:171px;height:19px;"></div><div style="top:190px;height:19px;"></div><div style="top:209px;height:19px;"></div><div style="top:228px;height:19px;"></div><div style="top:247px;height:19px;"></div><div style="top:266px;height:19px;"></div><div style="top:285px;height:19px;"></div><div style="top:304px;height:19px;"></div><div style="top:323px;height:19px;"></div><div style="top:342px;height:19px;"></div><div style="top:361px;height:19px;"></div><div style="top:380px;height:19px;"></div><div style="top:399px;height:19px;"></div><div style="top:418px;height:19px;"></div><div style="top:437px;height:19px;"></div><div style="top:456px;height:19px;"></div><div style="top:475px;height:19px;"></div><div style="top:494px;height:19px;"></div><div style="top:513px;height:19px;"></div><div style="top:532px;height:19px;"></div><div style="top:551px;height:19px;"></div><div style="top:570px;height:19px;"></div><div style="top:589px;height:19px;"></div><div style="top:608px;height:19px;"></div><div style="top:627px;height:19px;"></div><div style="top:646px;height:19px;"></div><div style="top:665px;height:19px;"></div><div style="top:684px;height:19px;"></div><div style="top:703px;height:19px;"></div><div style="top:722px;height:19px;"></div><div style="top:741px;height:19px;"></div><div style="top:760px;height:19px;"></div><div style="top:779px;height:19px;"></div><div style="top:798px;height:19px;"></div><div style="top:817px;height:19px;"></div><div style="top:836px;height:19px;"></div><div style="top:855px;height:19px;"></div><div style="top:874px;height:19px;"></div><div style="top:893px;height:19px;"></div><div style="top:912px;height:19px;"></div><div style="top:931px;height:19px;"></div><div style="top:950px;height:19px;"></div><div style="top:969px;height:19px;"></div><div style="top:988px;height:19px;"></div><div style="top:1007px;height:19px;"></div><div style="top:1026px;height:19px;"></div><div style="top:1045px;height:19px;"></div><div style="top:1064px;height:19px;"></div><div style="top:1083px;height:19px;"></div><div style="top:1102px;height:19px;"></div><div style="top:1121px;height:19px;"></div><div style="top:1140px;height:19px;"></div><div style="top:1159px;height:19px;"></div><div style="top:1178px;height:19px;"></div><div style="top:1197px;height:19px;"></div><div style="top:1216px;height:19px;"></div><div style="top:1235px;height:19px;"></div><div style="top:1254px;height:19px;"></div><div style="top:1273px;height:19px;"></div><div style="top:1292px;height:19px;"></div><div style="top:1311px;height:19px;"></div><div style="top:1330px;height:19px;"></div><div style="top:1349px;height:19px;"></div><div style="top:1368px;height:19px;"></div><div style="top:1387px;height:19px;"></div><div style="top:1406px;height:19px;"></div><div style="top:1425px;height:19px;"></div><div style="top:1444px;height:19px;"></div><div style="top:1463px;height:19px;"></div><div style="top:1482px;height:19px;"></div><div style="top:1501px;height:19px;"></div><div style="top:1520px;height:19px;"></div><div style="top:1539px;height:19px;"></div><div style="top:1558px;height:19px;"></div><div style="top:1577px;height:19px;"></div><div style="top:1596px;height:19px;"></div><div style="top:1615px;height:19px;"><div class="current-line current-line-margin-both" style="width:6px"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="6" style="position: absolute; overflow: hidden; left: 6px; width: 790px; height: 1644px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1.67772e+07px; height: 1644px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 922px;"><div style="top:0px;height:19px;"></div><div style="top:19px;height:19px;"></div><div style="top:38px;height:19px;"></div><div style="top:57px;height:19px;"></div><div style="top:76px;height:19px;"></div><div style="top:95px;height:19px;"></div><div style="top:114px;height:19px;"></div><div style="top:133px;height:19px;"></div><div style="top:152px;height:19px;"></div><div style="top:171px;height:19px;"></div><div style="top:190px;height:19px;"></div><div style="top:209px;height:19px;"></div><div style="top:228px;height:19px;"></div><div style="top:247px;height:19px;"></div><div style="top:266px;height:19px;"></div><div style="top:285px;height:19px;"></div><div style="top:304px;height:19px;"></div><div style="top:323px;height:19px;"></div><div style="top:342px;height:19px;"></div><div style="top:361px;height:19px;"></div><div style="top:380px;height:19px;"></div><div style="top:399px;height:19px;"></div><div style="top:418px;height:19px;"></div><div style="top:437px;height:19px;"></div><div style="top:456px;height:19px;"></div><div style="top:475px;height:19px;"></div><div style="top:494px;height:19px;"></div><div style="top:513px;height:19px;"></div><div style="top:532px;height:19px;"></div><div style="top:551px;height:19px;"></div><div style="top:570px;height:19px;"></div><div style="top:589px;height:19px;"></div><div style="top:608px;height:19px;"></div><div style="top:627px;height:19px;"></div><div style="top:646px;height:19px;"></div><div style="top:665px;height:19px;"></div><div style="top:684px;height:19px;"></div><div style="top:703px;height:19px;"></div><div style="top:722px;height:19px;"></div><div style="top:741px;height:19px;"></div><div style="top:760px;height:19px;"></div><div style="top:779px;height:19px;"></div><div style="top:798px;height:19px;"></div><div style="top:817px;height:19px;"></div><div style="top:836px;height:19px;"></div><div style="top:855px;height:19px;"></div><div style="top:874px;height:19px;"></div><div style="top:893px;height:19px;"></div><div style="top:912px;height:19px;"></div><div style="top:931px;height:19px;"></div><div style="top:950px;height:19px;"></div><div style="top:969px;height:19px;"></div><div style="top:988px;height:19px;"></div><div style="top:1007px;height:19px;"></div><div style="top:1026px;height:19px;"></div><div style="top:1045px;height:19px;"></div><div style="top:1064px;height:19px;"></div><div style="top:1083px;height:19px;"></div><div style="top:1102px;height:19px;"></div><div style="top:1121px;height:19px;"></div><div style="top:1140px;height:19px;"></div><div style="top:1159px;height:19px;"></div><div style="top:1178px;height:19px;"></div><div style="top:1197px;height:19px;"></div><div style="top:1216px;height:19px;"></div><div style="top:1235px;height:19px;"></div><div style="top:1254px;height:19px;"></div><div style="top:1273px;height:19px;"></div><div style="top:1292px;height:19px;"></div><div style="top:1311px;height:19px;"></div><div style="top:1330px;height:19px;"></div><div style="top:1349px;height:19px;"></div><div style="top:1368px;height:19px;"></div><div style="top:1387px;height:19px;"></div><div style="top:1406px;height:19px;"></div><div style="top:1425px;height:19px;"></div><div style="top:1444px;height:19px;"></div><div style="top:1463px;height:19px;"></div><div style="top:1482px;height:19px;"></div><div style="top:1501px;height:19px;"></div><div style="top:1520px;height:19px;"></div><div style="top:1539px;height:19px;"></div><div style="top:1558px;height:19px;"></div><div style="top:1577px;height:19px;"></div><div style="top:1596px;height:19px;"></div><div style="top:1615px;height:19px;"><div class="current-line current-line-exact" style="width:922px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 1644px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="8" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 922px; height: 1644px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;joblib</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;np</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.ensemble&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;IsolationForest</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">generate_synthetic_network_dataset</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk16">num_samples</span><span class="mtk1">:&nbsp;</span><span class="mtk16">int</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk12">5000</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;-&gt;&nbsp;pd.DataFrame:</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"""Generates&nbsp;synthetic&nbsp;network&nbsp;authentication&nbsp;&amp;&nbsp;tr</span><span class="mtk21">affic&nbsp;flow&nbsp;data.</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;Features:</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;failed_attempts:&nbsp;failed&nbsp;login&nbsp;count&nbsp;within</span><span class="mtk21">&nbsp;60&nbsp;seconds</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;session_duration_sec:&nbsp;duration&nbsp;of&nbsp;active&nbsp;c</span><span class="mtk21">onnection</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;bytes_sent_kb:&nbsp;outbound&nbsp;payload&nbsp;volume</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;port_number:&nbsp;destination&nbsp;port&nbsp;(22=SSH,&nbsp;80=</span><span class="mtk21">HTTP,&nbsp;443=HTTPS,&nbsp;8080=Alt)</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk21">&nbsp;&nbsp;&nbsp;&nbsp;"""</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;np.random.seed</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">42</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;98%&nbsp;Normal&nbsp;traffic&nbsp;patterns</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;num_normal&nbsp;=&nbsp;</span><span class="mtk14">int</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">num_samples&nbsp;*&nbsp;</span><span class="mtk12">0.98</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;normal_failed&nbsp;=&nbsp;np.random.poisson</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">lam=</span><span class="mtk12">0.2</span><span class="mtk1">,&nbsp;size=num_normal</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;normal_duration&nbsp;=&nbsp;np.random.exponential</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">scale=</span><span class="mtk12">120</span><span class="mtk1">,&nbsp;size=num_normal</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;+&nbsp;</span><span class="mtk12">5</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;normal_bytes&nbsp;=&nbsp;np.random.normal</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">loc=</span><span class="mtk12">150</span><span class="mtk1">,&nbsp;scale=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;size=num_normal</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.clip</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">10</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1000</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;normal_ports&nbsp;=&nbsp;np.random.choice</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">80</span><span class="mtk1">,&nbsp;</span><span class="mtk12">443</span><span class="mtk1">,&nbsp;</span><span class="mtk12">8080</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;size=num_normal,&nbsp;p=</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0.4</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0.55</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0.05</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;normal_df&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk1 bracket-highlighting-0">(</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"failed_attempts"</span><span class="mtk1">:&nbsp;normal_failed,</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"session_duration_sec"</span><span class="mtk1">:&nbsp;normal_duration,</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"bytes_sent_kb"</span><span class="mtk1">:&nbsp;normal_bytes,</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"port_number"</span><span class="mtk1">:&nbsp;normal_ports,</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"is_anomaly"</span><span class="mtk1">:&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">}</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;2%&nbsp;Malicious&nbsp;/&nbsp;Anomalous&nbsp;traffic&nbsp;(Brute-force&nbsp;SS</span><span class="mtk8">H,&nbsp;data&nbsp;exfiltration,&nbsp;abnormal&nbsp;ports)</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;num_anom&nbsp;=&nbsp;num_samples&nbsp;-&nbsp;num_normal</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;anom_failed&nbsp;=&nbsp;np.random.randint</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">5</span><span class="mtk1">,&nbsp;</span><span class="mtk12">30</span><span class="mtk1">,&nbsp;size=num_anom</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;anom_duration&nbsp;=&nbsp;np.random.exponential</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">scale=</span><span class="mtk12">10</span><span class="mtk1">,&nbsp;size=num_anom</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;+&nbsp;</span><span class="mtk12">0.5</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;anom_bytes&nbsp;=&nbsp;np.random.exponential</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">scale=</span><span class="mtk12">2000</span><span class="mtk1">,&nbsp;size=num_anom</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;+&nbsp;</span><span class="mtk12">500</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;anom_ports&nbsp;=&nbsp;np.random.choice</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">22</span><span class="mtk1">,&nbsp;</span><span class="mtk12">23</span><span class="mtk1">,&nbsp;</span><span class="mtk12">3389</span><span class="mtk1">,&nbsp;</span><span class="mtk12">4444</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;size=num_anom</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;anom_df&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk1 bracket-highlighting-0">(</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"failed_attempts"</span><span class="mtk1">:&nbsp;anom_failed,</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"session_duration_sec"</span><span class="mtk1">:&nbsp;anom_duration,</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"bytes_sent_kb"</span><span class="mtk1">:&nbsp;anom_bytes,</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"port_number"</span><span class="mtk1">:&nbsp;anom_ports,</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"is_anomaly"</span><span class="mtk1">:&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">}</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;df&nbsp;=&nbsp;pd.concat</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk1">normal_df,&nbsp;anom_df</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;ignore_index=</span><span class="mtk6">True</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.sample</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">frac=</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.reset_index</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">drop=</span><span class="mtk6">True</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;df</span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">train_and_export_model</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"&gt;&gt;&gt;&nbsp;Generating&nbsp;synthetic&nbsp;dataset..."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1083px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;df&nbsp;=&nbsp;generate_synthetic_network_dataset</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">num_samples=</span><span class="mtk12">6000</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1102px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;df.to_csv</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"network_traffic_dataset.csv"</span><span class="mtk1">,&nbsp;index=</span><span class="mtk6">False</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1121px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"&gt;&gt;&gt;&nbsp;Saved&nbsp;'network_traffic_dataset.csv'&nbsp;(6000&nbsp;row</span><span class="mtk21">s)."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1140px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1159px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Features&nbsp;used&nbsp;for&nbsp;anomaly&nbsp;perception</span></span></div><div style="top:1178px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;feature_cols&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk21">"failed_attempts"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"session_duration_sec"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"bytes_sent_kb"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"port_number"</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1197px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;X&nbsp;=&nbsp;df</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">feature_cols</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1216px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1235px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"&gt;&gt;&gt;&nbsp;Training&nbsp;Isolation&nbsp;Forest&nbsp;model..."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1254px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;contamination&nbsp;approx&nbsp;2%</span></span></div><div style="top:1273px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;model&nbsp;=&nbsp;IsolationForest</span><span class="mtk1 bracket-highlighting-0">(</span></span></div><div style="top:1292px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_estimators=</span><span class="mtk12">100</span><span class="mtk1">,</span></span></div><div style="top:1311px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contamination=</span><span class="mtk12">0.02</span><span class="mtk1">,</span></span></div><div style="top:1330px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1">,</span></span></div><div style="top:1349px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_jobs=</span><span class="mtk12">-1</span></span></div><div style="top:1368px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1387px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;model.fit</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1406px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1425px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Serialize&nbsp;model&nbsp;&amp;&nbsp;expected&nbsp;feature&nbsp;order</span></span></div><div style="top:1444px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;model_artifact&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span></span></div><div style="top:1463px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"model"</span><span class="mtk1">:&nbsp;model,</span></span></div><div style="top:1482px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk21">"feature_cols"</span><span class="mtk1">:&nbsp;feature_cols,</span></span></div><div style="top:1501px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:1520px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;joblib.dump</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">model_artifact,&nbsp;</span><span class="mtk21">"detector_model.pkl"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1539px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"&gt;&gt;&gt;&nbsp;Successfully&nbsp;trained&nbsp;and&nbsp;exported&nbsp;artifact&nbsp;to</span><span class="mtk21">&nbsp;'detector_model.pkl'!\n"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1558px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1577px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1596px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk16">__name__</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk21">"__main__"</span><span class="mtk1">:</span></span></div><div style="top:1615px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;train_and_export_model</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget" role="listbox" widgetid="LightBulbWidget" style="position: absolute; display: none; visibility: hidden; max-width: 1332px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor  monaco-mouse-cursor-text " style="height: 19px; top: 1615px; left: 216px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="visible scrollbar horizontal" style="position: absolute; width: 776px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 664px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="2055" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 1644px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 1644px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 1644px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 796px;"></div><textarea data-mprt="7" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content" aria-required="false" tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 1615px; left: 6px; width: 76992px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 796px;"><div class="sticky-widget" widgetid="editor.contrib.stickyScrollWidget" style="width: 782px; position: absolute; right: 50%; top: 0px; display: none;"><div class="sticky-widget-line-numbers" role="none" style="width: 6px;"></div><div class="sticky-widget-lines-scrollable" style="--vscode-editorStickyScroll-scrollableWidth: 908px;"><div class="sticky-widget-lines" role="list" style="left: 0px;"></div></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesGlyphHoverWidget" style="position: absolute;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div><div data-mprt="9" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 1644px;"><div class="minimap-shadow-hidden" style="height: 1644px;"></div><canvas width="0" height="2055" style="position: absolute; left: 0px; width: 0px; height: 1644px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="2055" style="position: absolute; left: 0px; width: 0px; height: 1644px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 27px; width: 150px; z-index: 50; display: none; visibility: hidden; max-width: 1536px;"><div class="monaco-sash vertical" style="left: 148px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 25px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div data-mprt="5" class="overflowingOverlayWidgets"></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; right: 50%; top: 0px;"></div></div></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$739266375$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$739266375$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button focused" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-2 output_text"><pre>&gt;&gt;&gt; Generating synthetic dataset...
&gt;&gt;&gt; Saved 'network_traffic_dataset.csv' (6000 rows).
&gt;&gt;&gt; Training Isolation Forest model...
&gt;&gt;&gt; Successfully trained and exported artifact to 'detector_model.pkl'!

</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$739266375$--><div class="footer-links">
      <colab-footer-links><template shadowrootmode="open"><!----><!--?lit$739266375$--><!---->
        <!--?lit$739266375$-->
        <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links" aria-label="Colab paid products Link will open in a new tab"><!--?lit$739266375$-->Colab paid products</a>
      <!----><!---->
        <!--?lit$739266375$--> - 
        <a target="_blank" href="https://colab.research.google.com/cancel-subscription" aria-label="Cancel contracts here Link will open in a new tab"><!--?lit$739266375$-->Cancel contracts here</a>
      <!----><!--?--></template></colab-footer-links>
    </div>
        </div>
      </colab-scroller>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$739266375$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$739266375$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$739266375$--><md-icon-button id="tab-pane-2-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize"><div class="resizer-thumb"></div>
        <!--?lit$739266375$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$739266375$--><colab-tab-pane class="layout vertical grow" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" aria-labelledby="tab-title-3hbsLj2K_Jnt" draggable="true" tabindex="0" class="selected-tab" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$739266375$--><div class="indicator"></div>
      </div>
      <!--?lit$739266375$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$739266375$--><div class="colab-tab-title">
      <!--?lit$739266375$-->
      <span id="tab-title-3hbsLj2K_Jnt"><!--?lit$739266375$--><!--?lit$739266375$-->Release notes<!--?--></span>
    </div> <!--?lit$739266375$--><md-icon-button class="tab-close" data-aria-label="Close" title="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon></md-icon-button> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$739266375$--><!--?--></div>
      <!--?lit$739266375$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$739266375$--><md-icon-button id="tab-pane-1-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow selected-tab relnotes-tab"><colab-scroller class="layout vertical grow"> <div><span><p>Please follow our <a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab" target="_blank" rel="nofollow" aria-label="blog Link will open in a new tab">blog</a> to see more
information about new features, tips and tricks, and featured notebooks such as
<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fnoteworthy-notebooks-3-analyzing-a-bank-failure-with-colab-d23b372de313" target="_blank" rel="nofollow" aria-label="Analyzing a Bank Failure with Colab Link will open in a new tab">Analyzing a Bank Failure with Colab</a>.</p>
<h3>2026-08-06</h3>
<ul>
<li><p>Check out the new <a href="https://colab.research.google.com/" target="_blank" rel="nofollow" aria-label="Colab Home page Link will open in a new tab">Colab Home page</a>!</p>
</li>
<li><p>Jimothy mode! (Settings &gt; Miscellaneous &gt; check "Jimothy Mode")</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>dask 2026.6.0 -&gt; 2026.7.0</li>
<li>diffusers 0.38.0 -&gt; 0.39.0</li>
<li>earthengine-api 1.7.30 -&gt; 1.7.35</li>
<li>google-adk 1.29.0 -&gt; 2.4.0</li>
<li>google-auth 2.47.0 -&gt; 2.49.0</li>
<li>google-genai 1.68.0 -&gt; 2.11.0</li>
<li>gradio 5.50.0 -&gt; 6.20.0</li>
<li>highspy 1.14.0 -&gt; 1.15.1</li>
<li>huggingface_hub 1.19.0 -&gt; 1.23.0</li>
<li>jupyter_server 2.18.2 -&gt; 2.20.0</li>
<li>langsmith 0.8.15 -&gt; 0.10.2</li>
<li>narwhals 2.22.1 -&gt; 2.24.0</li>
<li>openai 2.41.1 -&gt; 2.45.0</li>
<li>opencv-python 4.13.0.92 -&gt; 5.0.0.93</li>
<li>pandas-datareader 0.10.0 -&gt; 0.11.1</li>
<li>python-utils 3.9.1 -&gt; 4.0.0</li>
<li>transformers 5.12.0 -&gt; 5.13.1</li>
<li>uvicorn 0.49.0 -&gt; 0.51.0</li>
<li>wandb 0.27.2 -&gt; 0.28.0</li>
<li>xgboost 3.2.0 -&gt; 3.3.0</li>
</ul>
</li>
</ul>
<h3>2026-06-18</h3>
<ul>
<li><p>Launched Visualization Mode: Build dashboards using plain language with
Gemini.</p>
</li>
<li><p>Launched fullscreen sharing: Share interactive outputs and dashboards instantly with one link. <a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fannouncing-visualization-mode-fullscreen-output-sharing-in-google-colab-5f53ffa51494" target="_blank" rel="nofollow" aria-label="Learn more here Link will open in a new tab">Learn more here</a>.</p>
</li>
<li><p>Bring the power of Colab straight to your terminal!
Access GPUs/TPUs, run scripts remotely, and supercharge your AI agents with the new Colab CLI. <a href="https://www.google.com/url?q=https%3A%2F%2Fdevelopers.googleblog.com%2Fintroducing-the-google-colab-cli%2F" target="_blank" rel="nofollow" aria-label="Learn more here Link will open in a new tab">Learn more here</a></p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.13.0 -&gt; 1.14.0</li>
<li>aiohttp 3.13.5 -&gt; 3.14.1</li>
<li>bigframes 2.39.0 -&gt; 2.42.0</li>
<li>blosc2 4.1.2 -&gt; 4.4.5</li>
<li>dask 2026.3.0 -&gt; 2026.6.0</li>
<li>diffusers 0.37.1 -&gt; 0.38.0</li>
<li>fastcore 1.12.42 -&gt; 1.13.3</li>
<li>greenlet 3.4.0 -&gt; 3.5.1</li>
<li>huggingface_hub 1.11.0 -&gt; 1.19.0</li>
<li>jupyter_server 2.14.0 -&gt; 2.18.2</li>
<li>kagglehub 1.0.0 -&gt; 1.0.2</li>
<li>kagglesdk 0.1.20 -&gt; 0.1.23</li>
<li>langchain 1.2.15 -&gt; 1.3.9</li>
<li>langchain-core 1.3.1 -&gt; 1.4.7</li>
<li>langgraph 1.1.9 -&gt; 1.2.5</li>
<li>langsmith 0.7.34 -&gt; 0.8.15</li>
<li>narwhals 2.20.0 -&gt; 2.22.1</li>
<li>openai 2.32.0 -&gt; 2.41.1</li>
<li>panel 1.8.10 -&gt; 1.9.3</li>
<li>PyDrive2 1.21.1 -&gt; 1.21.3</li>
<li>safetensors 0.7.0 -&gt; 0.8.0</li>
<li>sentence-transformers 5.4.1 -&gt; 5.5.1</li>
<li>shap 0.51.0 -&gt; 0.52.0</li>
<li>torchaudio 2.10.0 -&gt; 2.11.0</li>
<li>torch 2.10.0 -&gt; 2.11.0</li>
<li>torchvision 0.25.0 -&gt; 0.26.0</li>
<li>tornado 6.5.1 -&gt; 6.5.7</li>
<li>transformers 5.0.0 -&gt; 5.12.0</li>
<li>uvicorn 0.46.0 -&gt; 0.49.0</li>
<li>wandb 0.26.1 -&gt; 0.27.2</li>
</ul>
</li>
</ul>
<h3>2026-05-06</h3>
<ul>
<li><p>Try these two new features in Colab. <a href="https://www.google.com/url?q=https%3A%2F%2Fblog.google%2Finnovation-and-ai%2Ftechnology%2Fdevelopers-tools%2Fcolab-updates%2F" target="_blank" rel="nofollow" aria-label="Learn more here Link will open in a new tab">Learn more here</a>:</p>
<ul>
<li>Custom Instructions- customized agent context that travel with your notebook, so anyone you share it with gets the tailored AI experience you designed.</li>
<li>Learn Mode- a pre-tuned custom Instruciton that makes Gemini in Colab act as a personal tutor for learning new material.</li>
</ul>
</li>
<li><p>VS Code Extension updates</p>
<ul>
<li>RAM and disk usage resource monitoring.</li>
<li>Compute consumption in the status bar.</li>
<li>Terminal support.</li>
<li>Import Colab Drive notebooks.</li>
</ul>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>attrs 25.4.0 -&gt; 26.1.0</li>
<li>bigframes 2.38.0 -&gt; 2.39.0</li>
<li>bigquery-magics 0.10.3 -&gt; 0.14.0</li>
<li>dask 2026.1.2 -&gt; 2026.3.0</li>
<li>dataproc-spark-connect 1.0.2 -&gt; 1.1.0</li>
<li>google-adk 1.27.1 -&gt; 1.29.0</li>
<li>gymnasium 1.2.3 -&gt; 1.3.0</li>
<li>highspy 1.13.1 -&gt; 1.14.0</li>
<li>holidays 0.93 -&gt; 0.95</li>
<li>huggingface_hub 1.7.1 -&gt; 1.11.0</li>
<li>kaggle 2.0.0 -&gt; 2.0.2</li>
<li>mcp 1.26.0 -&gt; 1.27.0</li>
<li>narwhals 2.18.0 -&gt; 2.20.0</li>
<li>openai 2.28.0 -&gt; 2.32.0</li>
<li>peft 0.18.1 -&gt; 0.19.1</li>
<li>tensorboard 2.19.0 -&gt; 2.20.0</li>
<li>tensorflow 2.19.0 -&gt; 2.20.0</li>
<li>tensorflow-text 2.19.0 -&gt; 2.20.1</li>
<li>tf_keras 2.19.0 -&gt; 2.20.0</li>
</ul>
</li>
<li><p>Package inclusions</p>
<ul>
<li>ydf_tf 2.20.0</li>
</ul>
</li>
</ul>
<h3>2026-03-25</h3>
<ul>
<li><p>Google Colab's marketing site (<a href="https://www.google.com/url?q=http%3A%2F%2Fcolab.google" target="_blank" rel="nofollow" aria-label="http://colab.google Link will open in a new tab">http://colab.google</a>) has a fresh new look!</p>
</li>
<li><p>Added support for Nvidia RTX Pro 6000 Blackwell Server Edition GPUs on G4 machines. With a peak rating of 960 BF16 TFLOPs (~50% more than the A100-80G) and 96 GB of VRAM (20% more than the A100-80G), it’s the most efficient high-performance GPU we’ve ever offered. Select "G4 GPU" in the runtime type menu.</p>
</li>
<li><p>Colab's new Open Source MCP Server gives your local agents programmatic access to control the entire notebook development lifecycle. Use your local agent to build, run, and visualize in the browser. (<a href="https://github.com/googlecolab/colab-mcp" target="_blank" rel="nofollow" aria-label="GitHub Repo Link will open in a new tab">GitHub Repo</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.12.0 -&gt; 1.13.0</li>
<li>bigframes 2.35.0 -&gt; 2.38.0</li>
<li>blosc2 4.0.0 -&gt; 4.1.2</li>
<li>diffusers 0.36.0 -&gt; 0.37.0</li>
<li>google-adk 1.25.1 -&gt; 1.27.1</li>
<li>google-genai 1.64.0 -&gt; 1.67.0</li>
<li>h5py 3.15.1 -&gt; 3.16.0</li>
<li>huggingface_hub 1.4.1 -&gt; 1.7.1</li>
<li>kaggle 1.7.4.5 -&gt; 2.0.0</li>
<li>kagglehub 0.3.13 -&gt; 1.0.0</li>
<li>keras 3.10.0 -&gt; 3.13.2</li>
<li>keras-hub 0.21.1 -&gt; 0.26.0</li>
<li>keras-nlp 0.21.1 -&gt; 0.26.0</li>
<li>narwhals 2.17.0 -&gt; 2.18.0</li>
<li>openai 2.23.0 -&gt; 2.28.0</li>
<li>sentence-transformers 5.2.3 -&gt; 5.3.0</li>
<li>shap 0.50.0 -&gt; 0.51.0</li>
</ul>
</li>
</ul>
<h3>2026-02-23</h3>
<ul>
<li><p>Enterprise Runtimes are now available in Colab - get the familiar notebook you love with the enterprise power you need (<a href="https://www.google.com/url?q=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2026%2F01%2Fgoogle-colab-support-is-now-available-in-pycharm-2025-3-2%2F" target="_blank" rel="nofollow" aria-label="learn more Link will open in a new tab">learn more</a>):</p>
<ul>
<li>Persistent runtimes</li>
<li>Configurable hardware &amp; powerful GPUs</li>
<li>Seamless Vertex AI &amp; BigQuery integration</li>
<li>Scale from idea to production without leaving your notebook.</li>
</ul>
</li>
<li><p>Launched official PyCharm Colab extension. <a href="https://www.google.com/url?q=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2026%2F01%2Fgoogle-colab-support-is-now-available-in-pycharm-2025-3-2%2F" target="_blank" rel="nofollow" aria-label="Learn more. Link will open in a new tab">Learn more.</a></p>
</li>
<li><p>Published Colab's CPU Docker runtime image to us-docker.pkg.dev/colab-images/public/cpu-runtime</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 2.31.0 -&gt; 2.35.0</li>
<li>bokeh 3.7.3 -&gt; 3.8.2</li>
<li>cudf-cu12 25.10.0 -&gt; 26.2.1</li>
<li>cudf-polars-cu12 25.10.0 -&gt; 26.2.1</li>
<li>cuml-cu12 25.10.0 -&gt; 26.2.0</li>
<li>cupy-cuda12x 13.6.0 -&gt; 14.0.1</li>
<li>dask 2025.9.1 -&gt; 2026.1.2</li>
<li>dask-cuda 25.10.0 -&gt; 26.2.0</li>
<li>dask-cudf-cu12 25.10.0 -&gt; 26.2.1</li>
<li>fastapi: 0.123.10 -&gt; 0.133.0</li>
<li>google-adk 1.21.0 -&gt; 1.25.1</li>
<li>google-auth 2.43.0 -&gt; 2.47.0</li>
<li>google-genai 1.55.0 -&gt; 1.64.0</li>
<li>holidays 0.88 -&gt; 0.91</li>
<li>holidays: 0.88 -&gt; 0.91</li>
<li>huggingface-hub: 0.36.0 -&gt; 1.4.1</li>
<li>mcp 1.25.0 -&gt; 1.26.0</li>
<li>narwhals 2.15.0 -&gt; 2.17.0</li>
<li>nx-cugraph-cu12 25.10.0 -&gt; 26.2.0</li>
<li>openai 2.15.0 -&gt; 2.23.0</li>
<li>opencv-python: 4.12.0.88 -&gt; 4.13.0.92</li>
<li>polars 1.31.0 -&gt; 1.35.2</li>
<li>prophet 1.2.1 -&gt; 1.3.0</li>
<li>pylibraft-cu12 25.10.0 -&gt; 26.2.0</li>
<li>pytensor 2.36.3 -&gt; 2.37.0</li>
<li>raft-dask-cu12 25.10.0 -&gt; 26.2.0</li>
<li>torch 2.9.0 -&gt; 2.10.0</li>
<li>torchaudio 2.9.0 -&gt; 2.10.0</li>
<li>torchcodec 0.8.0 -&gt; 0.10.0</li>
<li>torchvision 0.24.0 -&gt; 2.25.0</li>
<li>transformers: 4.57.6 -&gt; 5.0.0</li>
<li>wandb 0.24.0 -&gt; 0.25.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>cucim-cu12</li>
<li>cuvs-cu12</li>
</ul>
</li>
</ul>
<h3>2026-01-20</h3>
<ul>
<li>Launched Data Explorer - a new feature that lets you search Kaggle datasets,
models, and competitions directly from a Colab notebook!</li>
<li>Gemini 3 is now available in Colab.</li>
<li>In addition to being available in VS Code, Colab is also available for use
in Antigravity, Cursor, and Windsurf via the Open VSX Registry!</li>
<li>H100 is being rolled out for more users.</li>
<li>Launched a new modern design for the Colab UI.</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 1.11.0 -&gt; 1.12.0</li>
<li>astropy 7.1.1 -&gt; 7.2.0</li>
<li>bigframes 2.28.0 -&gt; 2.31.0</li>
<li>cachetools 5.5.2 -&gt; 6.2.4</li>
<li>dataproc-spark-connect 0.8.3 -&gt; 1.0.1</li>
<li>diffusers 0.35.2 -&gt; 0.36.0</li>
<li>flax 0.10.7 -&gt; 0.11.2</li>
<li>google 2.0.3 -&gt; 3.0.0</li>
<li>google-adk 1.17.0 -&gt; 1.21.0</li>
<li>google-auth 2.38.0 -&gt; 2.43.0</li>
<li>google-genai 1.49.0 -&gt; 1.55.0</li>
<li>gradio 5.49.1 -&gt; 5.50.0</li>
<li>holidays 0.84 -&gt; 0.88</li>
<li>humanize 4.14.0 -&gt; 4.15.0</li>
<li>langchain 0.3.27 -&gt; 1.2.4</li>
<li>langsmith 0.4.42 -&gt; 0.6.4</li>
<li>lxml 5.4.0 -&gt; 6.0.2</li>
<li>mcp 1.21.0 -&gt; 1.25.0</li>
<li>narwhals 2.11.0 -&gt; 2.15.0</li>
<li>networkx 3.5 -&gt; 3.6.1</li>
<li>openai 1.109.1 -&gt; 2.15.0</li>
<li>peft 0.17.1 -&gt; 0.18.1</li>
<li>prophet 1.1.7 -&gt; 1.2.1</li>
<li>pydot 3.0.4 -&gt; 4.0.1</li>
<li>pymc 5.26.1 -&gt; 5.27.0</li>
<li>pyspark 3.5.1 -&gt; 4.0.1</li>
<li>pytensor 2.35.1 -&gt; 2.36.3</li>
<li>sentence-transformers 5.1.2 -&gt; 5.2.0</li>
<li>sympy 1.13.3 -&gt; 1.14.0</li>
<li>tenacity 8.5.0 -&gt; 9.1.2</li>
<li>torch 2.8.0 -&gt; 2.9.0</li>
<li>torchaudio 2.8.0 -&gt; 2.9.0</li>
<li>torchvision 0.23.0 -&gt; 0.24.0</li>
<li>wandb 0.22.3 -&gt; 0.24.0</li>
<li>xarray 2025.10.1 -&gt; 2025.12.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>grain 0.2.15</li>
</ul>
<h3>2025-11-13</h3>
<ul>
<li><strong>VS Code Extension</strong>: Connect to Colab runtimes from VS Code
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DGoogle.colab" target="_blank" rel="nofollow" aria-label="extension Link will open in a new tab">extension</a>,
<a href="https://github.com/googlecolab/colab-vscode" target="_blank" rel="nofollow" aria-label="repository Link will open in a new tab">repository</a>).</li>
<li><strong>"Notebook Info" Moved:</strong> The "Notebook Info" command has been moved from
the View dropdown menu to the File dropdown menu, aligning with other
Workspace products.</li>
<li><strong>Improved Error Handling</strong>: Error messages when failing to create a Colab
session have been improved.</li>
<li><strong>Improved Accessibility</strong>: Tooltips in the table of contents has been
updated.</li>
<li><strong>Add prompt cells</strong>: It is now possible to add prompt cells within
Colab
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fall-colab-users-now-get-access-to-gemini-and-gemma-models-via-colab-python-library-at-no-cost-a392599977c4" target="_blank" rel="nofollow" aria-label="Blog Link will open in a new tab">Blog</a>).</li>
<li><strong>OAuth flow</strong>: Improved support and error handling during OAuth flow.</li>
<li><strong>Open in Colab</strong>: Released version 1.2.1 of the (<a href="https://github.com/googlecolab/open_in_colab" target="_blank" rel="nofollow" aria-label="Open in Colab Chrome Extension Link will open in a new tab">Open in Colab Chrome Extension</a>).</li>
<li><strong>Gradio app deployment</strong>: Publish Gradio apps to Cloud Run with just a few
clicks. Launch a Gradio app from a Colab notebook and click on the "Deploy
to Cloud Run" button.</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>bigframes 2.24.0 -&gt; 2.28.0</li>
<li>cuda-python 12.6.2.post1 -&gt; 12.9.4</li>
<li>cudf-cu12 25.6.0 -&gt; 25.10.0</li>
<li>cudf-polars-cu12 25.6.0 -&gt; 25.10.0</li>
<li>cuml-cu12 25.6.0 -&gt; 25.10.0</li>
<li>cupy-cuda12x 13.3.0 -&gt; 13.6.0</li>
<li>dask 2025.5.0 -&gt; 2025.9.1</li>
<li>dask-cuda 25.6.0 -&gt; 25.10.0</li>
<li>dask-cudf-cu12 25.6.0 -&gt; 25.10.0</li>
<li>distributed 2025.5.0 -&gt; 2025.9.1</li>
<li>flax 0.10.6 -&gt; 0.10.7</li>
<li>google-adk 1.14.1 -&gt; 1.17.0</li>
<li>google-genai 1.41.0 -&gt; 1.49.0</li>
<li>h5py 3.14.0 -&gt; 3.15.1</li>
<li>highspy 1.11.0 -&gt; 1.12.0</li>
<li>holidays 0.82 -&gt; 0.84</li>
<li>huggingface-hub 0.35.3 -&gt; 0.36.0</li>
<li>humanize 4.13.0 -&gt; 4.14.0</li>
<li>idna 3.10 -&gt; 3.11</li>
<li>jax 0.5.3 -&gt; 0.7.2</li>
<li>jaxlib 0.5.3 -&gt; 0.7.2</li>
<li>jupyter_core 5.8.1 -&gt; 5.9.1</li>
<li>libcugraph-cu12 25.6.0 -&gt; 25.10.0</li>
<li>libcuml-cu12 25.6.0 -&gt; 25.10.0</li>
<li>mcp 1.16.0 -&gt; 1.21.0</li>
<li>narwhals 2.7.0 -&gt; 2.11.0</li>
<li>numba-cuda 0.11.0 -&gt; 0.19.1</li>
<li>nx-cugraph-cu12 25.6.0 -&gt; 25.10.0</li>
<li>pandas-gbq 0.29.2 -&gt; 0.30.0</li>
<li>polars 1.25.2 -&gt; 1.31.0</li>
<li>pymc 5.25.1 -&gt; 5.26.1</li>
<li>pytensor 2.31.7 -&gt; 2.35.1</li>
<li>raft-dask-cu12 25.6.0 -&gt; 25.10.0</li>
<li>shap 0.48.0 -&gt; 0.50.0</li>
<li>tornado 6.4.2 -&gt; 6.5.1</li>
<li>uvicorn 0.37.0 -&gt; 0.38.0</li>
<li>xgboost 3.0.5 -&gt; 3.1.1</li>
</ul>
<p>Library Upgrades</p>
<ul>
<li>openjdk-11-* -&gt; openjdk-17-*</li>
</ul>
<h3>2025-10-14</h3>
<ul>
<li>Great news for Colab subscribers, we’ve lowered costs for our most popular accelerators. CPU runtime costs were increased slightly to match costs. Enjoy savings on:<ul>
<li>GPUs (A100, L4, T4) up to 13% cost reduction</li>
<li>TPUs (V28, V5E1, V6E1) up to 10% cost reduction</li>
</ul>
</li>
<li>Launched dynamic suggestions in Colab AI, giving context aware suggested prompts to users conversing with Gemini in Colab.</li>
<li>Launched <a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1965169070485180676" target="_blank" rel="nofollow" aria-label="High memory A100s Link will open in a new tab">High memory A100s</a> offering double the GPU and system RAM.</li>
<li>Launched <a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1970990455925113118" target="_blank" rel="nofollow" aria-label="Runtime Version Selector Link will open in a new tab">Runtime Version Selector</a>, giving users enhanced reproducibility and letting you reliably execute old code.</li>
<li>Launched <a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1970990455925113118" target="_blank" rel="nofollow" aria-label="Slideshow mode improvements Link will open in a new tab">Slideshow mode improvements</a> like starting a slideshow anywhere in the notebook.</li>
<li>Added Copy Cell Output command to the cell output menu.</li>
<li>Python package upgrades<ul>
<li>bigframes 2.17.0 -&gt; 2.24.0</li>
<li>cffi 1.17.1 -&gt; 2.0.0</li>
<li>google-adk 1.12.0 -&gt; 1.14.1</li>
<li>google-genai 1.31.0 -&gt; 1.41.0</li>
<li>gradio 5.43.1 -&gt; 5.49.0</li>
<li>huggingface-hub 0.34.4 -&gt; 0.35.3</li>
<li>jupyter-client 6.1.12 -&gt; 7.4.9</li>
<li>jupyter-console 6.1.0 -&gt; 6.6.3</li>
<li>jupyter-server 1.16.0 -&gt; 2.14.0</li>
<li>kagglehub 0.3.12 -&gt; 0.3.13</li>
<li>Markdown 3.8.2 -&gt; 3.9</li>
<li>mcp 1.13.1 -&gt; 1.16.0</li>
<li>narwhals 2.2.0 -&gt; 2.7.0</li>
<li>openai 1.101.0 -&gt; 1.109.1</li>
<li>tiktoken 0.11.0 -&gt; 0.12.0</li>
<li>tokenizers 0.21.4 -&gt; 0.22.1</li>
<li>transformers 4.55.4 -&gt; 4.57.0</li>
<li>uvicorn 0.35.0 -&gt; 0.37.0</li>
<li>wandb 0.21.1 -&gt; 0.22.2</li>
<li>xarray 2025.8.0 -&gt; 2025.10.1</li>
</ul>
</li>
</ul>
<h3>2025-08-27</h3>
<ul>
<li><p>Python runtimes upgraded to Python 3.12. <a href="https://github.com/googlecolab/colabtools/issues/5483" target="_blank" rel="nofollow" aria-label="GitHub Link will open in a new tab">GitHub</a></p>
</li>
<li><p>Julia runtimes upgraded to Julia 1.11. <a href="https://github.com/googlecolab/colabtools/issues/5408" target="_blank" rel="nofollow" aria-label="GitHub Link will open in a new tab">GitHub</a></p>
</li>
<li><p>Launched <a href="https://www.google.com/url?q=https%3A%2F%2Fblog.google%2Foutreach-initiatives%2Feducation%2Fcolab-higher-education%2F" target="_blank" rel="nofollow" aria-label="Interactive Slideshow Mode for lectures Link will open in a new tab">Interactive Slideshow Mode for lectures</a>. It provides a better viewing experience for presentations making lessons more dynamic.</p>
</li>
<li><p>Launched <a href="https://www.google.com/url?q=https%3A%2F%2Fblog.google%2Foutreach-initiatives%2Feducation%2Fcolab-higher-education%2F" target="_blank" rel="nofollow" aria-label="AI toggle per notebook Link will open in a new tab">AI toggle per notebook</a>.
As requested by instructors, Colab now supports a toggle for disabling AI
features at a notebook level to allow instructors and students to focus on
learning without assistance.</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.9.0 -&gt; 1.10.1</li>
<li>aiohttp 3.11.15 -&gt; 3.12.15</li>
<li>anyio 4.9.0 -&gt; 4.10.0</li>
<li>bigframes 2.11.0 -&gt; 2.17.0</li>
<li>bigquery-magics 0.10.1 -&gt; 0.10.3</li>
<li>blosc2 3.6.1 -&gt; 3.7.2</li>
<li>datasets 2.14.4 -&gt; 4.0.0</li>
<li>diffusers 0.34.0 -&gt; 0.35.1</li>
<li>fastai 2.7.19 -&gt; 2.8.4</li>
<li>gcsfs 2025.3.0 -&gt; 2025.7.0</li>
<li>google-genai 1.26.0 -&gt; 1.31.0</li>
<li>gradio 5.38.0 -&gt; 5.43.1</li>
<li>h2 4.2.0 -&gt; 4.3.0</li>
<li>huggingface-hub 0.33.4 -&gt; 0.34.4</li>
<li>imbalanced-learn 0.13.0 -&gt; 0.14.0</li>
<li>jax 0.5.2 -&gt; 0.5.3</li>
<li>jaxlib 0.5.1 -&gt; 0.5.3</li>
<li>keras 3.8.0 -&gt; 3.10.0</li>
<li>ml-dtypes 0.4.1 -&gt; 0.5.3</li>
<li>openai 1.97.0 -&gt; 1.101.0</li>
<li>peft 0.16.0 -&gt; 0.17.1</li>
<li>polars 1.25.0 -&gt; 1.25.2</li>
<li>pymc 5.24.1 -&gt; 5.25.1</li>
<li>pyzmq 24.0.1 -&gt; 26.2.1</li>
<li>requests 2.32.3 -&gt; 2.32.4</li>
<li>scipy 1.16.0 -&gt; 1.16.1</li>
<li>sentence-transformers 4.1.0 -&gt; 5.1.0</li>
<li>tensorboard 2.18.0 -&gt; 2.19.0</li>
<li>tensorflow 2.18.0 -&gt; 2.19.0</li>
<li>tf_keras 2.18.0 -&gt; 2.19.0</li>
<li>timm 1.0.17 -&gt; 1.0.19</li>
<li>torch 2.6.0 -&gt; 2.8.0</li>
<li>torchaudio 2.6.0 -&gt; 2.8.0</li>
<li>torchvision 0.19.0 -&gt; 0.23.0</li>
<li>transformers 4.53.2 -&gt; 4.55.4</li>
<li>triton 3.2.0 -&gt; 3.4.0</li>
<li>wandb 0.21.0 -&gt; 0.21.1</li>
<li>xarray 2025.7.1 -&gt; 2025.8.0</li>
<li>xgboost 3.0.2 -&gt; 3.0.4</li>
</ul>
</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>anywidget 0.9.18</li>
<li>google-adk 1.12.0</li>
<li>mcp 1.13.1</li>
</ul>
<p>Python package removals</p>
<ul>
<li>PyDrive 1.3.1</li>
</ul>
<h3>2025-07-22</h3>
<ul>
<li><p>Terminal is now available to all users, free of charge! (<a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1937248640252412093" target="_blank" rel="nofollow" aria-label="X Link will open in a new tab">X</a>, <a href="https://colab.research.google.com/notebooks/snippets/colab_models_as_a_service.ipynb" target="_blank" rel="nofollow" aria-label="Colab Notebook Link will open in a new tab">Colab Notebook</a>)</p>
</li>
<li><p>The new Colab AI experience is now available to all users. This version has an agentic collaborator run with Gemini 2.5 Flash and enhances productivity with features like iterative querying, a next-gen data science agent, code transformation, and more to significantly improve coding workflows for developers. (<a href="https://www.google.com/url?q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Fnew-ai-first-google-colab-now-available-to-everyone%2F" target="_blank" rel="nofollow" aria-label="Blog Link will open in a new tab">Blog</a>, <a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1937557047186530782" target="_blank" rel="nofollow" aria-label="X Link will open in a new tab">X</a>)</p>
</li>
<li><p>Introducing our new google.colab.ai library! Pro &amp; Pro+ subscribers can access powerful Gemini and Gemma models with just a few lines of code- no set up or API key required! Try it out! (<a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1944895802180296826" target="_blank" rel="nofollow" aria-label="X Link will open in a new tab">X</a>, <a href="https://colab.research.google.com/notebooks/snippets/colab_models_as_a_service.ipynb" target="_blank" rel="nofollow" aria-label="Colab Notebook Link will open in a new tab">Colab Notebook</a>)</p>
</li>
<li><p>Big news for data science in higher ed! 🚀 Colab now offers 1-year Pro subscriptions free of charge for verified US students/faculty, interactive Slideshow Mode for lectures, &amp; an AI toggle per notebook. Enhance teaching &amp; learning in the upcoming academic year! Read all about it <a href="https://www.google.com/url?q=https%3A%2F%2Fgoo.gle%2F40pxnl1" target="_blank" rel="nofollow" aria-label="here Link will open in a new tab">here</a>. (<a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1946269436207669274" target="_blank" rel="nofollow" aria-label="X Link will open in a new tab">X</a>)</p>
</li>
<li><p>Gemini CLI installed on runtimes. Try it out in the Terminal! (<a href="https://github.com/google-gemini/gemini-cli" target="_blank" rel="nofollow" aria-label="github Link will open in a new tab">github</a>, <a href="https://www.google.com/url?q=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40google%2Fgemini-cli" target="_blank" rel="nofollow" aria-label="npm Link will open in a new tab">npm</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.7.0 -&gt; 1.9.0</li>
<li>bigframes 2.6.0 -&gt; 2.11.0</li>
<li>bigquery-magics 0.9.0 -&gt; 0.10.1</li>
<li>cudf-cu12 25.2.1 -&gt; 25.6.0</li>
<li>cuml-cu12 25.2.1 -&gt; 25.6.0</li>
<li>dask 2024.12.1 -&gt; 25.5.0</li>
<li>dask-cuda 25.2.0 -&gt; 25.6.0</li>
<li>dask-cudf 25.2.2 -&gt; 25.6.0</li>
<li>dataproc-spark-connect 0.7.5 -&gt; 0.8.3</li>
<li>debugpy 1.8.0 -&gt; 1.8.15</li>
<li>diffusers 0.33.1 -&gt; 0.34.0</li>
<li>distributed 2024.12.1 -&gt; 25.5.0</li>
<li>duckdb 1.2.2 -&gt; 1.3.2</li>
<li>earthengine-api 1.5.19 -&gt; 1.5.24</li>
<li>gcsfs 2025.3.2 -&gt; 25.7.0</li>
<li>geopandas 1.0.1 -&gt; 1.1.1</li>
<li>google-genai 1.20.0 -&gt; 1.26.0</li>
<li>gradio 5.31.0 -&gt; 5.38.0</li>
<li>narwhals 1.42.0 -&gt; 1.48.0</li>
<li>numba-cuda 0.2.0 -&gt; 0.11.0</li>
<li>openai 1.86.0 -&gt; 1.97.0</li>
<li>opencv-python 4.11.0.86 -&gt; 4.12.0.88</li>
<li>pillow 11.2.1 -&gt; 11.3.0</li>
<li>polars 1.21.0 -&gt; 1.25.0</li>
<li>pymc 5.23.0 -&gt; 5.24.1</li>
<li>scipy 1.15.3 -&gt; 1.16.0</li>
<li>shap 0.47.2 -&gt; 0.48.0</li>
<li>timm 1.0.15 -&gt; 1.0.17</li>
<li>transformers 4.52.4 -&gt; 4.53.2</li>
<li>urllib3 2.4.0 -&gt; 2.5.0</li>
<li>wandb 0.20.1 -&gt; 0.21.0</li>
<li>xarray 2025.3.1 -&gt; 25.7.1</li>
<li>xgboost 2.1.4 -&gt; 3.0.2</li>
</ul>
</li>
</ul>
<h3>2025-06-16</h3>
<ul>
<li><p>At Google I/O Colab announced a new, reimagined AI-first Colab, bringing a
powerful agentic collaborator into the notebook. Learn more <a href="https://www.google.com/url?q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Ffully-reimagined-ai-first-google-colab%2F" target="_blank" rel="nofollow" aria-label="here Link will open in a new tab">here</a>.</p>
</li>
<li><p>Huggingface integration: We’ve partnered with Hugging Face to add “Open in
Colab” support for all models on the Hugging Face Hub. Now you can directly
launch a Colab notebook from any model card, making it easier than ever to
experiment with and evaluate models. View the announcement <a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Flaunch-hugging-face-models-in-colab-for-faster-ai-exploration-bee261978cf9" target="_blank" rel="nofollow" aria-label="blog Link will open in a new tab">blog</a> to learn more</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.6.0 -&gt; 1.7.0</li>
<li>bigframes 2.3.0 -&gt; 2.6.0</li>
<li>earthengine-api 1.5.14 -&gt; 1.5.19</li>
<li>gdal 3.6.4 -&gt; 3.8.4</li>
<li>google-genai 1.14.0 -&gt; 1.20.0</li>
<li>grpcio 1.71.0 -&gt; 1.73.0</li>
<li>highspy 1.10.0 -&gt; 1.11.0</li>
<li>huggingface-hub 0.31.1 -&gt; 0.33.0</li>
<li>narwhals 1.38.2 -&gt; 1.42.0</li>
<li>networkx 3.4.2 -&gt; 3.5</li>
<li>openai 1.78.0 -&gt; 1.86.0</li>
<li>pandas-gbq 0.28.0 -&gt; 0.29.1</li>
<li>panel 1.6.3 -&gt; 1.7.1</li>
<li>pymc 5.22.0 -&gt; 5.23.0</li>
<li>pytensor 2.30.3 -&gt; 2.31.3</li>
<li>spacy 3.8.5 -&gt; 3.8.7</li>
<li>wandb 0.19.11 -&gt; 0.20.1</li>
<li>zipp 3.21 -&gt; 3.23</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>gradio 5.31.0</li>
</ul>
</li>
</ul>
<h3>2025-05-12</h3>
<ul>
<li><p>Pro+ Subscriptions give 600 CCUs now: <a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FGoogleColab%2Fstatus%2F1913312272967209357" target="_blank" rel="nofollow" aria-label="https://x.com/GoogleColab/status/1913312272967209357 Link will open in a new tab">https://x.com/GoogleColab/status/1913312272967209357</a></p>
</li>
<li><p>Launched Colab's fastest deep learning accelerator: v6e-1 (Trillium) TPUs!! 2x the high bandwidth memory as v5e-1 (32GB) and a whopping peak rating of 918 BF16 TFLOPS (nearly 3x A100)!️ Try them out with JAX &amp; Flax in our <a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fnotebooks%2Fjax_tpu_v6e1.ipynb" target="_blank" rel="nofollow" aria-label="example notebook Link will open in a new tab">example notebook</a></p>
</li>
<li><p>Enabled UTF-8 mode by default for Python</p>
</li>
<li><p>Added CUDA.jl and Pluto.jl for Julia</p>
</li>
<li><p>Enabled OpenCL for LightGBM</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>accelerate 1.5.2 -&gt; 1.6.0</li>
<li>bigframes 1.42.0 -&gt; 2.3.0</li>
<li>bokeh 3.6.3 -&gt; 3.7.2</li>
<li>cudf-cu12 24.12.0 -&gt; 25.2.1</li>
<li>google-genai 1.9.0 -&gt; 1.14.0</li>
<li>highspy 1.9.0 -&gt; 1.10.0</li>
<li>holidays 0.69 -&gt; 0.72</li>
<li>huggingface-hub 0.30.1 -&gt; 0.31.1</li>
<li>lxml 5.3.1 -&gt; 5.4.0</li>
<li>nx_cugraph_cu12 24.12.0 -&gt; 25.2.1</li>
<li>openai 1.70.0 -&gt; 1.78.0</li>
<li>peft 0.14.0 -&gt; 0.15.2</li>
<li>polars 1.14.0 -&gt; 1.21.0</li>
<li>pyomo 6.8.2 -&gt; 6.9.2</li>
<li>scipy 1.14.1 -&gt; 1.15.3</li>
<li>sentence-transformers 3.4.1 -&gt; 4.1.0</li>
<li>transformers 4.50.3 -&gt; 4.51.3</li>
<li>urllib3 2.3.0 -&gt; 2.4.0</li>
<li>xarray 2025.1.2 -&gt; 2025.3.1</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>dataproc-spark-connect 0.7.3</li>
<li>libpysal 4.13.0</li>
<li>lightgbm</li>
<li>stumpy 1.13.0</li>
<li>torchao 0.10.0</li>
<li>torchtune 0.6.1</li>
<li>tsfresh 0.21.0</li>
</ul>
</li>
</ul>
<h3>2025-04-09</h3>
<ul>
<li>Colab Data Science Agent <a href="https://www.google.com/url?q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Fdata-science-agent-in-colab-with-gemini%2F" target="_blank" rel="nofollow" aria-label="launched Link will open in a new tab">launched</a>!</li>
<li>Julia language runtimes available with GPU and TPU support <a href="https://github.com/googlecolab/colabtools/issues/5151" target="_blank" rel="nofollow" aria-label="GitHub Link will open in a new tab">GitHub</a>.</li>
<li>Now your popular Kaggle datasets are cached for quick retrieval.</li>
<li>Upgraded Colab runtimes to Python 3.11.</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>bigframes 1.29.0 -&gt; 1.42.0</li>
<li>TensorFlow 2.17.1 -&gt; 2.18.0</li>
<li>tensorboard 2.17.1 -&gt; 2.18.0</li>
<li>keras 3.5.0 -&gt; 3.8.0</li>
<li>torch 2.5.1 -&gt; 2.6.0</li>
<li>torchaudio 2.5.1 -&gt; 2.6.0</li>
<li>torchvision 0.20.1 -&gt; 0.21.0</li>
<li>fastai 2.7.18 -&gt; 2.7.19</li>
<li>ipykernel 5.5.6 -&gt; 6.17.1</li>
<li>google-genai 0.3.0 -&gt; 1.9.0</li>
<li>google-auth 2.27.0 -&gt; 2.38.0</li>
<li>Tornado 6.3.3 -&gt; 6.4.2</li>
<li>jax 0.4.33 -&gt; 0.5.2</li>
<li>accelerate 1.2.1 -&gt; 1.5.2</li>
<li>transformers 4.47.1 -&gt; 4.50.3</li>
<li>openai 1.57.4 -&gt; 1.70.0</li>
<li>kagglehub 0.3.6 -&gt; 0.3.11</li>
<li>earthengine-api 1.4.3 -&gt; 1.5.9</li>
<li>google-cloud-bigquery 3.29.0 -&gt; 3.31.0</li>
<li>bigquery-magics 0.8.1 -&gt; 0.9.0</li>
<li>NumPy 1.26.4 -&gt; 2.0.2</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>cuml-cu12 24.12.0</li>
</ul>
<h3>2025-01-13</h3>
<ul>
<li>Released version 1.2.0 of the (<a href="https://github.com/googlecolab/open_in_colab" target="_blank" rel="nofollow" aria-label="Open in Colab Chrome Extension Link will open in a new tab">Open in Colab Chrome Extension</a>).</li>
<li>Released minimizable comments with indicators next to cell.</li>
<li>TPU v5e-1 Runtimes are now available for selection (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1869458629230993619" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>).</li>
<li>GPU prices were decreased (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1869458629230993619" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>).</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 1.1.1 -&gt; 1.2.1</li>
<li>aiohttp 3.10.10 -&gt; 3.11.11</li>
<li>altair 4.2.2 -&gt; 5.5.0</li>
<li>bigframes 1.25.0 -&gt; 1.29.0</li>
<li>cmake 3.30.5 -&gt; 3.31.2</li>
<li>cvxpy 1.5.3 -&gt; 3.6.0</li>
<li>earthengine-api 1.2.0 -&gt; 1.4.3</li>
<li>folium 0.18.0 -&gt; 0.19.3</li>
<li>holidays 0.60 -&gt; 0.63</li>
<li>huggingface-hub 0.26.2 -&gt; 0.27.0</li>
<li>jsonpickle 3.4.2 -&gt; 4.0.1</li>
<li>kagglehub 0.3.3 -&gt; 0.3.6</li>
<li>keras 3.4.1 -&gt; 3.5.0</li>
<li>matplotlib 3.8.0 -&gt; 3.10.0</li>
<li>openai 1.54.3 -&gt; 1.57.4</li>
<li>pymc 5.18.0 -&gt; 5.19.1</li>
<li>safetensors 0.4.5 -&gt; 0.5.0</li>
<li>scikit-image 0.24.0 -&gt; 0.25.0</li>
<li>scikit-learn 1.5.2 -&gt; 1.6.0</li>
<li>sentence-transformers 3.2.1 -&gt; 3.3.1</li>
<li>tensorflow 2.17.0 -&gt; 2.17.1</li>
<li>torch 2.5.0 -&gt; 2.5.1</li>
<li>torchaudio 2.5.0 -&gt; 2.5.1</li>
<li>torchvision 0.20.0 -&gt; 0.20.1</li>
<li>transformers 4.46.2 -&gt; 4.47.1</li>
<li>wandb 0.18.6 -&gt; 0.19.1</li>
<li>xarray 2024.10.0 -&gt; 2024.11.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>google-genai 0.3.0</li>
</ul>
<h3>2024-11-11</h3>
<ul>
<li>Users can now import Gemini API keys from AI Studio into their user secrets,
all in Colab
(<a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FOfficialLoganK%2Fstatus%2F1854584985849618812" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>).</li>
<li>Increased limit to 1000 characters for requests to Gemini in Chat and
Generate windows.</li>
<li>Improved saving notebook to GitHub flow.</li>
<li>Updated Gemini spark icon to be colorful.</li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fdocs.astral.sh%2Fuv%2F" target="_blank" rel="nofollow" aria-label="uv Link will open in a new tab"><code>uv</code></a> is pre-installed on the PATH for faster
package installs.</li>
<li>Fixed bugs<ul>
<li>Dropdown text for GitHub repository not visible
<a href="https://github.com/googlecolab/colabtools/issues/4901" target="_blank" rel="nofollow" aria-label="#4901 Link will open in a new tab">#4901</a>.</li>
<li>Pre-installed California housing dataset README not correct
<a href="https://github.com/googlecolab/colabtools/issues/4862" target="_blank" rel="nofollow" aria-label="#4862 Link will open in a new tab">#4862</a>.</li>
<li>Backend execution error for scheduled notebook
<a href="https://github.com/googlecolab/colabtools/issues/4850" target="_blank" rel="nofollow" aria-label="#4850 Link will open in a new tab">#4850</a>.</li>
<li>Drive File Stream issues
<a href="https://github.com/googlecolab/colabtools/issues/3441" target="_blank" rel="nofollow" aria-label="#3441 Link will open in a new tab">#3441</a>.</li>
<li>Linking to the signup page does not preserve the authuser parameter.</li>
<li>Error messages in Gemini chat are not polished.</li>
<li>Clicking in Gemini chat feedback causes jitters the UI.</li>
<li>Hovering over a table of contents entry would show the menu icons for
all entries.</li>
<li>Surveys display over open dialogs.</li>
<li>Playground mode banner not shown on mobile.</li>
</ul>
</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 0.34.2 -&gt; 1.1.1</li>
<li>arviz 0.19.0 -&gt; 0.20.0</li>
<li>bigframes 1.18.0 -&gt; 1.25.0</li>
<li>bigquery-magics 0.2.0 -&gt; 0.4.0</li>
<li>bokeh 3.4.3 -&gt; 3.6.1</li>
<li>blosc 2.0.0 -&gt; 2.7.1</li>
<li>cloudpickle 2.2.1 -&gt; 3.1.0</li>
<li>cudf-cu12 24.4.1 -&gt; 24.10.1</li>
<li>dask 2024.8.0 -&gt; 24.10.0</li>
<li>debugpy 1.6.6 -&gt; 1.8.0</li>
<li>earthengine-api 1.0.0 -&gt; 1.2.0</li>
<li>folium 0.17.0 -&gt; 0.18.0</li>
<li>gscfs 2024.6.1 -&gt; 2024.10.0</li>
<li>geemap 0.34.3 -&gt; 0.35.1</li>
<li>holidays 0.57 -&gt; 0.60</li>
<li>huggingface-hub 0.24.7 -&gt; 0.26.2</li>
<li>kagglehub 0.3.0 -&gt; 0.3.3</li>
<li>lightgbm 4.4.0 -&gt; 4.5.0</li>
<li>lxml 4.9.4 -&gt; 5.3.0</li>
<li>matplotlib 3.7.1 -&gt; 3.8.0</li>
<li>mizani 0.11.4 -&gt; 0.13.0</li>
<li>networkx 3.3 -&gt; 3.4.2</li>
<li>nltk 3.8.1 -&gt; 3.9.1</li>
<li>pandas 2.1.4 -&gt; 2.2.2</li>
<li>pillow 10.4.0 -&gt; 11.0.0</li>
<li>plotnine 0.13.6 -&gt; 0.14.1</li>
<li>polars 1.6.0 -&gt; 1.9.0</li>
<li>protobuf 3.20.3 -&gt; 4.25.5</li>
<li>pyarrow 14.0.2 -&gt; 17.0.0</li>
<li>pydrive2 1.20.0 -&gt; 1.21.1</li>
<li>pymc 5.16.2 -&gt; 5.18.0</li>
<li>torch 2.4.1 -&gt; 2.5.0</li>
<li>torchaudio 2.4.1 -&gt; 2.5.0</li>
<li>torchvision 0.19.1 -&gt; 0.20.0</li>
<li>transformers 4.44.2 -&gt; 4.46.2</li>
<li>xarray 2024.9.0 -&gt; 2024.10.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>diffusers 0.31.0</li>
<li>gitpython 3.1.43</li>
<li>langchain 0.3.7</li>
<li>openai 1.54.3</li>
<li>pygit2 1.16.0</li>
<li>pyspark 3.5.3</li>
<li>sentence-transformers 3.2.1</li>
<li>timm 1.0.11</li>
<li>wandb 0.18.6</li>
</ul>
<p>Library and driver upgrades</p>
<ul>
<li>drivefs upgraded from 89.0.2 to 98.0.0</li>
</ul>
<h3>2024-09-23</h3>
<ul>
<li>Improved code snippet search</li>
<li>Updated Marketplace image and public local runtime container</li>
<li>Improved the look-and-feel of interactive form dropdowns and checkboxes</li>
<li>Fixed bugs<ul>
<li>activating the skip link caused the notebook to scroll out of view</li>
<li>toggling a checkbox too much caused the page to crash</li>
<li>lightning fast drags could cause orphaned tabs</li>
<li>custom widgets snippet would show for local runtimes</li>
</ul>
</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 0.32.1 -&gt; 0.34.2</li>
<li>arviz 0.18.0 -&gt; 0.19</li>
<li>autograd 1.6.2 -&gt; 1.7.0</li>
<li>bigframes 1.14.0 -&gt; 1.18.0</li>
<li>dask 2024.7.1 -&gt; 2024.8.0</li>
<li>distributed 2024.7.1 -&gt; 2024.8.0</li>
<li>duckdb 0.10.3 -&gt; 1.1.0</li>
<li>earthengine-api 0.1.416 -&gt; 1.0.0</li>
<li>flax 0.8.4 -&gt; 0.8.5</li>
<li>gdown 5.1.0 -&gt; 5.2.0</li>
<li>geemap 0.33.1 -&gt; 0.34.3</li>
<li>geopandas 0.14.4 -&gt; 1.0.1</li>
<li>google-cloud-aiplatform 1.59.0 -&gt; 1.67.1</li>
<li>google-cloud-bigquery-storage 2.25.0 -&gt; 2.26.0</li>
<li>holidays 0.54 -&gt; 0.57</li>
<li>huggingface-hub 0.23.5 -&gt; 0.24.7</li>
<li>ibis-framework 8.0.0 -&gt; 9.2.0</li>
<li>jax 0.4.26 -&gt; 0.4.33</li>
<li>jaxlib 0.4.26 -&gt; 0.4.33</li>
<li>kagglehub 0.2.9 -&gt; 0.3.0</li>
<li>lightgbm 4.4.0 -&gt; 4.5.0</li>
<li>matplotlib-venn 0.11.10 -&gt; 1.1.1</li>
<li>mizani 0.9.3 -&gt; 0.11.4</li>
<li>Pillow 9.4.0 -&gt; 10.4.0</li>
<li>plotly 5.15.0 -&gt; 5.24.1</li>
<li>plotnine 0.12.4 -&gt; 0.13.6</li>
<li>polars 0.20.2 -&gt; 1.6.0</li>
<li>progressbar2 4.2.0 -&gt; 4.5.0</li>
<li>PyDrive2 1.6.3 -&gt; 1.20.0</li>
<li>pymc 5.10.4 -&gt; 5.16.2</li>
<li>pytensor 2.18.6 -&gt; 2.25.4</li>
<li>scikit-image 0.23.2 -&gt; 0.24.0</li>
<li>scikit-learn 1.3.2 -&gt; 1.5.2</li>
<li>torch 2.3.1 -&gt; 2.4.1</li>
<li>torchaudio 2.3.1 -&gt; 2.4.1</li>
<li>torchvision 0.18.1 -&gt; 0.19.1</li>
<li>transformers 4.42.4 -&gt; 4.44.2</li>
<li>urllib3 2.0.7 -&gt; 2.2.3</li>
<li>xarray 2024.6.0 -&gt; 2024.9.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>bigquery-magics 0.2.0</li>
</ul>
<h3>2024-08-20</h3>
<ul>
<li><p>TPU memory usage and utilization can now be checked with <code>!tpu-info</code></p>
</li>
<li><p>Gemini Chat responses are now grounded in relevant sources</p>
</li>
<li><p>Added a new "Create Gemini API key" link in the user secrets panel</p>
</li>
<li><p>Added a new "Gemini: Creating a prompt" snippet and touched up the existing
"Gemini: Connecting to Gemini" snippet</p>
</li>
<li><p>Added the ability to specify custom placeholder text for various interactive
form params (see
<a href="https://colab.research.google.com/notebooks/forms.ipynb" target="_blank" rel="nofollow" aria-label="examples Link will open in a new tab">examples</a>)</p>
</li>
<li><p>Keyboard navigation a11y improvements to comments UI</p>
</li>
<li><p>Various minor rendering improvements to interactive forms UI</p>
</li>
<li><p>A11y improvements for the run button and header</p>
</li>
<li><p>Updated tooltip styling</p>
</li>
<li><p>A11y improvements for the file browser’s disk usage bar</p>
</li>
<li><p>On mobile, tooltips now trigger on long press</p>
</li>
<li><p>On mobile, release notes updates will no longer display automatically</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>astropy 5.3.4 -&gt; 6.1.2</li>
<li>bigframes 1.11.1 -&gt; 1.14.0</li>
<li>bokeh 3.3.4 -&gt; 3.4.3</li>
<li>dask 2023.8.1 -&gt; 2024.7.1</li>
<li>earthengine-api 0.1.412 -&gt; 0.1.416</li>
<li>geopandas 0.13.2 -&gt; 0.14.4</li>
<li>kagglehub 0.2.8 -&gt; 0.2.9</li>
<li>keras 2.15.0 -&gt; 3.4.1</li>
<li>lightgbm 4.1.0 -&gt; 4.4.0</li>
<li>malloy 2023.1067 -&gt; 2024.1067</li>
<li>numba 0.58.1 -&gt; 0.60.0</li>
<li>numpy 1.25.2 -&gt; 1.26.4</li>
<li>opencv-python 4.8.0.76 -&gt; 4.10.0.84</li>
<li>pandas 2.0.3 -&gt; 2.1.4</li>
<li>pandas-gbq 0.19.2 -&gt; 0.23.1</li>
<li>panel 1.3.8 -&gt; 1.4.5</li>
<li>requests 2.31.0 -&gt; 2.32.3</li>
<li>scikit-learn 1.2.2. -&gt; 1.3.2</li>
<li>scipy 1.11.4 -&gt; 1.13.1</li>
<li>tensorboard 2.15.2 -&gt; 2.17.0</li>
<li>tensorflow 2.15.0 -&gt; 2.17.0</li>
<li>tf-keras 2.15.1 -&gt; 2.17.0</li>
<li>xarray 2023.7.0 -&gt; 2024.6.0</li>
<li>xgboost 2.0.3 -&gt; 2.1.1</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>einops 0.8.0</li>
</ul>
</li>
</ul>
<h3>2024-07-22</h3>
<ul>
<li><p>You can now embed Google sheets directly into Colab to streamline interactions with data with InteractiveSheet.</p>
<p>Example:</p>
<pre><code><span><span class="mtk1">from&nbsp;google.colab&nbsp;import&nbsp;sheets</span></span><br><span><span class="mtk1">sh&nbsp;=&nbsp;sheets.InteractiveSheet()</span></span><br><span><span class="mtk1">df&nbsp;=&nbsp;sh.as_df()</span></span>
</code></pre></li>
<li><p>Fixed multiple rendering bugs in cell editors with wide text content (i.e. text is no longer hidden or clipped)</p>
</li>
<li><p>Fixed multiple accessibility issues in Colab's comments feature (e.g. proper keyboard focus management, added accessibility landmarks, etc)</p>
</li>
<li><p>Fixed bug where AI code generation would fail for extremely long broken code snippets</p>
</li>
<li><p>Fixed multiple scrollbar bugs in the user secrets panel</p>
</li>
<li><p>Added the ability for workspace admin to purchase Colab Pro and Pro+ Subscriptions for users</p>
</li>
<li><p>Fixed bug where user secrets couldn’t be moved to a tab</p>
</li>
<li><p>Fixed several focus management accessibility issues in tabs, the table of contents, the left toolbar, and the run button</p>
</li>
<li><p>Fixed bug where overflowing cells may be omitted when pasting from Google Sheets</p>
</li>
<li><p>Fixed bug where the generate code button did not activate on touch</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 1.9.0 -&gt; 1.11.1</li>
<li>cvxpy 1.3.4 -&gt; 1.5.2</li>
<li>earthengine-api 0.1.408 -&gt; 0.1.412</li>
<li>google-api-core 2.11.1 -&gt; 2.19.1</li>
<li>google-api-python-client 2.84.0 -&gt; 2.137.0</li>
<li>google-cloud-aiplatform 1.56.0 -&gt; 1.59.0</li>
<li>google-cloud-bigquery 3.21.0 -&gt; 3.25.0</li>
<li>google-cloud-core 2.3.3 -&gt; 2.4.1</li>
<li>google-cloud-datastore 2.15.2 -&gt; 2.19.0</li>
<li>google-cloud-firestore 2.11.1 -&gt; 2.16.1</li>
<li>google-cloud-functions 1.13.3 -&gt; 1.16.4</li>
<li>google-generativeai 0.5.4 -&gt; 0.7.2</li>
<li>kagglehub 0.2.5 -&gt; 0.2.8</li>
<li>pip 23.1.2 -&gt; 24.1.2</li>
<li>setuptools 67.7.2 -&gt; 71.0.4</li>
<li>sympy 1.12.1 -&gt; 1.13.1</li>
<li>torch 2.3.0 -&gt; 2.3.1</li>
<li>transformers 4.41.2 -&gt; 4.42.4</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>accelerate 0.32.1</li>
</ul>
</li>
</ul>
<h3>2024-06-18</h3>
<ul>
<li><p>Inline AI completions are now available to users on the free-of-charge tier</p>
</li>
<li><p>Reduced latency for LSP and terminal connections</p>
</li>
<li><p>Improved quality of inline completions</p>
</li>
<li><p>Visual improvements to switch controls across Colab</p>
</li>
<li><p>Various bug fixes, performance and a11y improvements to the user secrets
panel</p>
</li>
<li><p>Improved tooltip UX behavior</p>
</li>
<li><p>Improved behavior when copying data from Google Sheets and pasting in Colab</p>
</li>
<li><p>Scroll to cell fixes for single tabbed view and jump to cell command</p>
</li>
<li><p>Improved tab header behavior</p>
</li>
<li><p>A11y improvements for notebook-focused cells</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>torch 2.2.1 -&gt; 2.3.0</li>
<li>torchaudio 2.2.1 -&gt; 2.3.0</li>
<li>torchvision 0.17.1 -&gt; 0.18.0</li>
<li>torchtext 0.17.1 -&gt; 0.18.0</li>
<li>google-cloud-aiplatform 1.51.0 -&gt; 1.56.0</li>
<li>bigframes 1.5.0 -&gt; 1.8.0</li>
<li>regex 2023.12.25 -&gt; 2024.5.15</li>
</ul>
</li>
</ul>
<h3>2024-05-13</h3>
<ul>
<li><p>Code actions are now supported to automatically improve and refactor code. Code actions can be triggered by the keyboard shortcut "Ctrl/⌘ + ."</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 1.0.0 -&gt; 1.5.0</li>
<li>google-cloud-aiplatform 1.47.0 -&gt; 1.51.0</li>
<li>jax[tpu] 0.4.23 -&gt; 0.4.26</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>cudf 24.4.1</li>
</ul>
</li>
</ul>
<h3>2024-04-15</h3>
<ul>
<li><p>TPU v2 runtime is now available</p>
</li>
<li><p>L4 runtime is now available for paid users</p>
</li>
<li><p>New distributed fine-tuning Gemma tutorial on TPUs
(<a href="https://github.com/googlecolab/colabtools/blob/main/notebooks/Gemma_Distributed_Fine_tuning_on_TPU.ipynb" target="_blank" rel="nofollow" aria-label="GitHub Link will open in a new tab">GitHub</a>)</p>
</li>
<li><p>Symbol rename is now supported with keyboard shortcut F2</p>
</li>
<li><p>Fixed bug causing inability to re-upload deleted files</p>
</li>
<li><p>Fixed breaking bug in colabtools %upload_files_async</p>
</li>
<li><p>Added syntax highlighting to %%writefile cells</p>
</li>
<li><p>Cuda dependencies that come with Torch are cached for faster 
downloads for packages that require Torch and its dependencies (<a href="https://github.com/googlecolab/colabtools/issues/4491" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.24.0 -&gt; 1.0.0</li>
<li>duckdb 0.9.2 -&gt; 0.10.1</li>
<li>google-cloud-aiplatform 1.43.0 -&gt; 1.47.0</li>
<li>jax 0.4.23 -&gt; 0.4.26</li>
</ul>
</li>
</ul>
<h3>2024-03-13</h3>
<ul>
<li><p>Fixed bug that sometimes caused UserSecrets to move / disappear</p>
</li>
<li><p>Improved messaging for mounting drive in an unsupported environment
(<a href="https://github.com/googlecolab/colabtools/issues/4375" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>torch 2.1.0 -&gt; 2.2.1</li>
<li>torchaudio 2.1.0 -&gt; 2.2.1</li>
<li>torchvision 0.16.0 -&gt; 0.17.1</li>
<li>torchtext 0.16.0 -&gt; 0.17.1</li>
<li>PyMC 5.7.2 -&gt; 5.10.4</li>
<li>BigFrames 0.21.0 -&gt; 0.24.0</li>
<li>google-cloud-aiplatform 1.42.1 -&gt; 1.43.0</li>
<li>tornado 6.3.2 -&gt; 6.3.3</li>
</ul>
</li>
</ul>
<h3>2024-02-21</h3>
<ul>
<li><p>Try out Gemma on
<a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemma/docs/lora_tuning.ipynb" target="_blank" rel="nofollow" aria-label="Colab Link will open in a new tab">Colab</a>!</p>
</li>
<li><p>Allow unicode in form text inputs</p>
</li>
<li><p>Display documentation and link to source when displaying functions</p>
</li>
<li><p>Display image-like ndarrays as images</p>
</li>
<li><p>Improved UX around quick charts and execution error suggestions</p>
</li>
<li><p>Released Marketplace image for the month of February
(<a href="https://github.com/googlecolab/colabtools/issues/4254" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.19.2 -&gt; 0.21.0</li>
<li>regex 2023.6.3 -&gt; 2023.12.25</li>
<li>spacy 3.6.1 -&gt; 3.7.4</li>
<li>beautifulsoup4 4.11.2 -&gt; 4.12.3</li>
<li>tensorflow-probability 0.22.0 -&gt; 0.23.0</li>
<li>google-cloud-language 2.9.1 -&gt; 2.13.1</li>
<li>google-cloud-aiplatform 1.39.0 -&gt; 1.42.1</li>
<li>transformers 4.35.2 -&gt; 4..37.2</li>
<li>pyarrow 10.0.1 -&gt; 14.0.2</li>
</ul>
</li>
</ul>
<h3>2024-01-29</h3>
<ul>
<li><p>New
<a href="https://www.google.com/url?q=https%3A%2F%2Fwww.kaggle.com%2Fdiscussions%2Fproduct-feedback%2F470030" target="_blank" rel="nofollow" aria-label="Kaggle Notebooks &lt;&gt; Colab updates Link will open in a new tab">Kaggle Notebooks &lt;&gt; Colab updates</a>!
Now you can:</p>
<ul>
<li>Import directly from Colab without having to download/re-upload</li>
<li>Upload via link, by pasting Google Drive or Colab URLs</li>
<li>Export &amp; run Kaggle Notebooks on Colab with 1 click</li>
</ul>
</li>
<li><p>Try these notebooks that talk to Gemini:</p>
<ul>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FGemini_and_Stable_Diffusion.ipynb" target="_blank" rel="nofollow" aria-label="Gemini and Stable Diffusion Link will open in a new tab">Gemini and Stable Diffusion</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FLearning_with_Gemini_and_ChatGPT.ipynb" target="_blank" rel="nofollow" aria-label="Learning with Gemini and ChatGPT Link will open in a new tab">Learning with Gemini and ChatGPT</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FTalk_to_Gemini_with_Google%2527s_Speech_to_Text_API.ipynb" target="_blank" rel="nofollow" aria-label="Talk to Gemini with Google&#39;s Speech to Text API Link will open in a new tab">Talk to Gemini with Google's Speech to Text API</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FSell_lemonade_with_Gemini_and_Sheets.ipynb" target="_blank" rel="nofollow" aria-label="Sell lemonade with Gemini and Sheets Link will open in a new tab">Sell lemonade with Gemini and Sheets</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FGenerate_images_with_Gemini_and_Vertex.ipynb" target="_blank" rel="nofollow" aria-label="Generate images with Gemini and Vertex Link will open in a new tab">Generate images with Gemini and Vertex</a></li>
</ul>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>google-cloud-aiplatform 1.38.1 -&gt; 1.39.0</li>
<li>bigframes 0.18.0 -&gt; 0.19.2</li>
<li>polars 0.17.3 -&gt; 0.20.2</li>
<li>gdown 4.6.6 -&gt; 4.7.3
(<a href="https://github.com/googlecolab/colabtools/issues/4298" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>tensorflow-hub 0.15.0 -&gt; 0.16.0</li>
<li>flax 0.7.5 -&gt; 0.8.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>sentencepiece 0.1.99</li>
</ul>
</li>
</ul>
<h3>2024-01-08</h3>
<ul>
<li><p>Avoid nested scrollbars for large outputs by using
<code>google.colab.output.no_vertical_scroll()</code>
<a href="https://colab.research.google.com/gist/blois/635d82605b163fc8fbb8ae1128c7f388/no_vertical_scroll.ipynb" target="_blank" rel="nofollow" aria-label="Example notebook Link will open in a new tab">Example notebook</a></p>
</li>
<li><p>Fix <a href="https://github.com/googlecolab/colabtools/issues/4272" target="_blank" rel="nofollow" aria-label="bug Link will open in a new tab">bug</a> where
downloading models from Hugging Face could freeze</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>huggingface-hub 0.19.4 -&gt; 0.20.2</li>
<li>bigframes 0.17.0 -&gt; 0.18.0</li>
</ul>
</li>
</ul>
<h3>2023-12-18</h3>
<ul>
<li><p>Expanded access to AI coding has arrived in Colab across 175 locales for all
tiers of Colab users</p>
</li>
<li><p>Improvements to display of ML-based inline completions (for eligible
Pro/Pro+ users)</p>
</li>
<li><p>Started a series of
<a href="https://github.com/googlecolab/colabtools/tree/main/notebooks" target="_blank" rel="nofollow" aria-label="notebooks Link will open in a new tab">notebooks</a>
highlighting Gemini API capabilities</p>
</li>
<li><p>Enable ⌘/Ctrl+L to select the full line in an editor</p>
</li>
<li><p>Fixed <a href="https://github.com/googlecolab/colabtools/issues/4174" target="_blank" rel="nofollow" aria-label="bug Link will open in a new tab">bug</a> where we
weren't correctly formatting output from multiple execution results</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>CUDA 11.8 to CUDA 12.2</li>
<li>tensorflow 2.14.0 -&gt; 2.15.0</li>
<li>tensorboard 2.14.0 -&gt; 2.15.0</li>
<li>keras 2.14.0 -&gt; 2.15.0</li>
<li>Nvidia drivers 525.105.17 -&gt; 535.104.05</li>
<li>tensorflow-gcs-config 2.14.0 -&gt; 2.15.0</li>
<li>bigframes 0.13.0 -&gt; 0.17.0</li>
<li>geemap 0.28.2 -&gt; 0.29.6</li>
<li>pyarrow 9.0.0 -&gt; 10.0.1</li>
<li>google-generativeai 0.2.2 -&gt; 0.3.1</li>
<li>jax 0.4.20 —&gt; 0.4.23</li>
<li>jaxlib 0.4.20 —&gt; 0.4.23</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>kagglehub 0.1.4</li>
<li>google-cloud-aiplatform 1.38.1</li>
</ul>
</li>
</ul>
<h3>2023-11-27</h3>
<ul>
<li><p>Removed warning when calling <code>await</code> to make it render as code</p>
</li>
<li><p>Added "Run selection" to the cell context menu</p>
</li>
<li><p>Added highlighting for the <code>%%python</code> cell magic</p>
</li>
<li><p>Launched AI coding features for Pro/Pro+ users in more locales</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.12.0 -&gt; 0.13.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>transformers 4.35.2</li>
<li>google-generativeai 0.2.2</li>
</ul>
</li>
</ul>
<h3>2023-11-08</h3>
<ul>
<li><p>Launched Secrets, for safe storage of private keys on Colab
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1719798406195867814" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</p>
</li>
<li><p>Fixed issue where TensorBoard would not load
(<a href="https://github.com/googlecolab/colabtools/issues/3990" target="_blank" rel="nofollow" aria-label="#3990 Link will open in a new tab">#3990</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>lightgbm 4.0.0 -&gt; 4.1.0</li>
<li>bigframes 0.10.0 -&gt; 0.12.0</li>
<li>bokeh 3.2.2 -&gt; 3.3.0</li>
<li>duckdb 0.8.1 -&gt; 0.9.1</li>
<li>numba 0.56.4 -&gt; 0.58.1</li>
<li>tweepy 4.13.0 -&gt; 4.14.0</li>
<li>jax 0.4.16 -&gt; 0.4.20</li>
<li>jaxlib 0.4.16 -&gt; 0.4.20</li>
</ul>
</li>
</ul>
<h3>2023-10-23</h3>
<ul>
<li><p>Updated the <strong>Open notebook</strong> dialog for better usability and support for
smaller screen sizes</p>
</li>
<li><p>Added smart paste support for data from Google Sheets for R notebooks</p>
</li>
<li><p>Enabled showing release notes in a tab</p>
</li>
<li><p>Launched AI coding features for Pro/Pro+ users in Australia 🇦🇺 Canada 🇨🇦
India 🇮🇳 and Japan 🇯🇵
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1714322243659108376" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>earthengine-api 0.1.357 -&gt; 0.1.375</li>
<li>flax 0.7.2 -&gt; 0.7.4</li>
<li>geemap 0.27.4 -&gt; 0.28.2</li>
<li>jax 0.4.14 -&gt; 0.4.16</li>
<li>jaxlib 0.4.14 -&gt; 0.4.16</li>
<li>keras 2.13.1 -&gt; 2.14.0</li>
<li>tensorboard 2.13.0 -&gt; 2.14.1</li>
<li>tensorflow 2.13.0 -&gt; 2.14.0</li>
<li>tensorflow-gcs-config 2.13.0 -&gt; 2.14.0</li>
<li>tensorflow-hub 0.14.0 -&gt; 0.15.0</li>
<li>tensorflow-probability 0.20.1 -&gt; 0.22.0</li>
<li>torch 2.0.1 -&gt; 2.1.0</li>
<li>torchaudio 2.0.2 -&gt; 2.1.0</li>
<li>torchtext 0.15.2 -&gt; 0.16.0</li>
<li>torchvision 0.15.2 -&gt; 0.16.0</li>
<li>xgboost 1.7.6 -&gt; 2.0.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>bigframes 0.10.0</li>
<li>malloy 2023.1056</li>
</ul>
</li>
</ul>
<h3>2023-09-22</h3>
<ul>
<li>Added the ability to scope an AI generated suggestion to a specific Pandas
dataframe
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1699880260056322462" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</li>
<li>Added Colab link previews to Docs
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1701684666972205243" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</li>
<li>Added smart paste support for data from Google Sheets</li>
<li>Increased font size of dropdowns in interactive forms</li>
<li>Improved rendering of the notebook when printing</li>
<li>Python package upgrades<ul>
<li>tensorflow 2.12.0 -&gt; 2.13.0</li>
<li>tensorboard 2.12.3 -&gt; 2.13.0</li>
<li>keras 2.12.0 -&gt; 2.13.1</li>
<li>tensorflow-gcs-config 2.12.0 -&gt; 2.13.</li>
<li>scipy 1.10.1-&gt; 1.11.2</li>
<li>cython 0.29.6 -&gt; 3.0.2</li>
</ul>
</li>
<li>Python package inclusions<ul>
<li>geemap 0.26.0</li>
</ul>
</li>
</ul>
<h3>2023-08-18</h3>
<ul>
<li>Added "Change runtime type" to the menu in the connection button</li>
<li>Improved auto-reconnection to an already running notebook
(<a href="https://github.com/googlecolab/colabtools/issues/3764" target="_blank" rel="nofollow" aria-label="#3764 Link will open in a new tab">#3764</a>)</li>
<li>Increased the specs of our highmem machines for Pro users</li>
<li>Fixed <code>add-apt-repository</code> command on Ubuntu 22.04 runtime
(<a href="https://github.com/googlecolab/colabtools/issues/3867" target="_blank" rel="nofollow" aria-label="#3867 Link will open in a new tab">#3867</a>)</li>
<li>Python package upgrades<ul>
<li>bokeh 2.4.3 -&gt; 3.2.2</li>
<li>cmake 3.25.2 -&gt; 3.27.2</li>
<li>cryptography 3.4.8 -&gt; 41.0.3</li>
<li>dask 2022.12.1 -&gt; 2023.8.0</li>
<li>distributed 2022.12.1 -&gt; 2023.8.0</li>
<li>earthengine-api 0.1.358 -&gt; 0.1.364</li>
<li>flax 0.7.0 -&gt; 0.7.2</li>
<li>ipython-sql 0.4.0 -&gt; 0.5.0</li>
<li>jax 0.4.13 -&gt; 0.4.14</li>
<li>jaxlib 0.4.13 -&gt; 0.4.14</li>
<li>lightgbm 3.3.5 -&gt; 4.0.0</li>
<li>mkl 2019.0 -&gt; 2023.2.0</li>
<li>notebook 6.4.8 -&gt; 6.5.5</li>
<li>numpy 1.22.4 -&gt; 1.23.5</li>
<li>opencv-python 4.7.0.72 -&gt; 4.8.0.76</li>
<li>pillow 8.4.0 -&gt; 9.4.0</li>
<li>plotly 5.13.1 -&gt; 5.15.0</li>
<li>prettytable 0.7.2 -&gt; 3.8.0</li>
<li>pytensor 2.10.1 -&gt; 2.14.2</li>
<li>spacy 3.5.4 -&gt; 3.6.1</li>
<li>statsmodels 0.13.5 -&gt; 0.14.0</li>
<li>xarray 2022.12.0 -&gt; 2023.7.0</li>
</ul>
</li>
<li>Python package inclusions<ul>
<li>PyDrive2 1.6.3</li>
</ul>
</li>
</ul>
<h3>2023-07-21</h3>
<ul>
<li><p>Launched auto-plotting for dataframes, available using the chart button that
shows up alongside datatables
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fcolab-data-visualizations-made-easy-5e1918e5234e" target="_blank" rel="nofollow" aria-label="post Link will open in a new tab">post</a>)</p>
<img src="./train_files/chart_icon.png" alt="Chart button in Colab" width="40">
</li>
<li><p>Added a menu to the table of contents to support running a section or
collapsing/expanding sections
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Ftwo-new-ways-to-manage-cell-execution-fbad61b40882" target="_blank" rel="nofollow" aria-label="post Link will open in a new tab">post</a>)</p>
<img alt="Table of Contents running a section" src="./train_files/run_section.png" width="300">
</li>
<li><p>Added an option to automatically run the first cell or section, available
under Edit -&gt; Notebook settings
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Ftwo-new-ways-to-manage-cell-execution-fbad61b40882" target="_blank" rel="nofollow" aria-label="post Link will open in a new tab">post</a>)</p>
<img alt="Run first cell option" src="./train_files/auto_run_first_cell.png" width="300">
</li>
<li><p>Launched Pro/Pro+ to Algeria, Argentina, Chile, Ecuador, Egypt, Ghana,
Kenya, Malaysia, Nepal, Nigeria, Peru, Rwanda, Saudi Arabia, South Africa,
Sri Lanka, Tunisia, and Ukraine
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1674412460017700866" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</p>
</li>
<li><p>Added a command, "Toggle tab moves focus" for toggling tab trapping in the
editor (Tools -&gt; Command palette, "Toggle tab moves focus")</p>
</li>
<li><p>Fixed issue where <code>files.upload()</code> was sometimes returning an incorrect
filename (<a href="https://github.com/googlecolab/colabtools/issues/1550" target="_blank" rel="nofollow" aria-label="#1550 Link will open in a new tab">#1550</a>)</p>
</li>
<li><p>Fixed f-string syntax highlighting bug
(<a href="https://github.com/googlecolab/colabtools/issues/3802" target="_blank" rel="nofollow" aria-label="#3802 Link will open in a new tab">#3802</a>)</p>
</li>
<li><p>Disabled ambiguous characters highlighting for commonly used LaTeX
characters (<a href="https://github.com/googlecolab/colabtools/issues/3648" target="_blank" rel="nofollow" aria-label="#3648 Link will open in a new tab">#3648</a>)</p>
</li>
<li><p>Upgraded Ubuntu from 20.04 LTS to
<a href="https://www.google.com/url?q=https%3A%2F%2Fdiscourse.ubuntu.com%2Ft%2Fjammy-jellyfish-release-notes%2F24668" target="_blank" rel="nofollow" aria-label="22.04 LTS Link will open in a new tab">22.04 LTS</a></p>
</li>
<li><p>Updated the Colab Marketplace VM image</p>
</li>
<li><p>Python package upgrades:</p>
<ul>
<li>autograd 1.6.1 -&gt; 1.6.2</li>
<li>drivefs 76.0 -&gt; 77.0</li>
<li>flax 0.6.11 -&gt; 0.7.0</li>
<li>earthengine-api 0.1.357 -&gt; 0.1.358</li>
<li>GDAL 3.3.2-&gt;3.4.3</li>
<li>google-cloud-bigquery-storage 2.20.0 -&gt; 2.22.2</li>
<li>gspread-dataframe 3.0.8 -&gt; 3.3.1</li>
<li>holidays 0.27.1 -&gt; 0.29</li>
<li>jax 0.4.10 -&gt; jax 0.4.13</li>
<li>jaxlib 0.4.10 -&gt; jax 0.4.13</li>
<li>jupyterlab-widgets 3.0.7 -&gt; 3.0.8</li>
<li>nbformat 5.9.0 -&gt; 5.9.1</li>
<li>opencv-python-headless 4.7.0.72 -&gt; 4.8.0.74</li>
<li>pygame 2.4.0 -&gt; 2.5.0</li>
<li>spacy 3.5.3 -&gt; 3.5.4</li>
<li>SQLAlchemy 2.0.16 -&gt; 2.0.19</li>
<li>tabulate 0.8.10 -&gt; 0.9.0</li>
<li>tensorflow-hub 0.13.0 -&gt; 0.14.0</li>
</ul>
</li>
</ul>
<h3>2023-06-23</h3>
<ul>
<li>Launched AI coding features to subscribed users starting with Pro+ users in
the US (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1661056135196217346" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fblog.google%2Ftechnology%2Fdevelopers%2Fgoogle-colab-ai-coding-features%2F" target="_blank" rel="nofollow" aria-label="post Link will open in a new tab">post</a>)</li>
<li>Added the Kernel Selector in the Notebook Settings
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1671265645756039168" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</li>
<li>Fixed double space trimming issue in markdown
<a href="https://github.com/googlecolab/colabtools/issues/3766" target="_blank" rel="nofollow" aria-label="#3766 Link will open in a new tab">#3766</a></li>
<li>Fixed run button indicator not always centered
<a href="https://github.com/googlecolab/colabtools/issues/3609" target="_blank" rel="nofollow" aria-label="#3609 Link will open in a new tab">#3609</a></li>
<li>Fixed inconsistencies for automatic indentation on multi-line
<a href="https://github.com/googlecolab/colabtools/issues/3697" target="_blank" rel="nofollow" aria-label="#3697 Link will open in a new tab">#3697</a></li>
<li>Upgraded Python from 3.10.11 to 3.10.12</li>
<li>Python package updates:<ul>
<li>duckdb 0.7.1 -&gt; 0.8.1</li>
<li>earthengine-api 0.1.350 -&gt; 0.1.357</li>
<li>flax 0.6.9 -&gt; 0.6.11</li>
<li>google-cloud-bigquery 3.9.0 -&gt; 3.10.0</li>
<li>google-cloud-bigquery-storage 2.19.1 -&gt; 2.20.0</li>
<li>grpcio 1.54.0 -&gt; 1.56.0</li>
<li>holidays 0.25 -&gt; 0.27.1</li>
<li>nbformat 5.8.0 -&gt; 5.9.0</li>
<li>prophet 1.1.3 -&gt; 1.1.4</li>
<li>pydata-google-auth 1.7.0 -&gt; 1.8.0</li>
<li>spacy 3.5.2 -&gt; 3.5.3</li>
<li>tensorboard 2.12.2 -&gt; 2.12.3</li>
<li>xgboost 1.7.5 -&gt; 1.7.6</li>
</ul>
</li>
<li>Python package inclusions:<ul>
<li>gcsfs 2023.6.0</li>
<li>geopandas 0.13.2</li>
<li>google-cloud-bigquery-connection 1.12.0</li>
<li>google-cloud-functions 1.13.0</li>
<li>grpc-google-iam-v1 0.12.6</li>
<li>multidict 6.0.4</li>
<li>tensorboard-data-server 0.7.1</li>
</ul>
</li>
</ul>
<h3>2023-06-02</h3>
<ul>
<li>Released the new site <a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.google" target="_blank" rel="nofollow" aria-label="colab.google Link will open in a new tab">colab.google</a></li>
<li>Published Colab's Docker runtime image to
us-docker.pkg.dev/colab-images/public/runtime
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1663594080436375558" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Flocal-runtimes.html" target="_blank" rel="nofollow" aria-label="instructions Link will open in a new tab">instructions</a>)</li>
<li>Launched support for Google children accounts
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1661811016664231937" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</li>
<li>Launched DagsHub integration
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FTheRealDagsHub%2Fstatus%2F1658098271850749956" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fdagshub.com%2Fblog%2Fgoogle-colab-integration%2F" target="_blank" rel="nofollow" aria-label="post Link will open in a new tab">post</a>)</li>
<li>Upgraded to Monaco Editor Version 0.37.1</li>
<li>Fixed various Vim keybinding bugs</li>
<li>Fixed issue where the N and P letters sometimes couldn't be typed
(<a href="https://github.com/googlecolab/colabtools/issues/3664" target="_blank" rel="nofollow" aria-label="#3664 Link will open in a new tab">#3664</a>)</li>
<li>Fixed rendering support for compositional inputs
(<a href="https://github.com/googlecolab/colabtools/issues/3660" target="_blank" rel="nofollow" aria-label="#3660 Link will open in a new tab">#3660</a>,
<a href="https://github.com/googlecolab/colabtools/issues/3660" target="_blank" rel="nofollow" aria-label="#3679 Link will open in a new tab">#3679</a>)</li>
<li>Fixed lag in notebooks with lots of cells
(<a href="https://github.com/googlecolab/colabtools/issues/3676" target="_blank" rel="nofollow" aria-label="#3676 Link will open in a new tab">#3676</a>)</li>
<li>Improved support for R by adding a Runtime type notebook setting (Edit -&gt;
Notebook settings)</li>
<li>Improved documentation for connecting to a local runtime (Connect -&gt; Connect
to a local runtime)</li>
<li>Python package updates:<ul>
<li>holidays 0.23 -&gt; 0.25</li>
<li>jax 0.4.8 -&gt; 0.4.10</li>
<li>jaxlib 0.4.8 -&gt; 0.4.10</li>
<li>pip 23.0.1 -&gt; 23.1.2</li>
<li>tensorflow-probability 0.19.0 -&gt; 0.20.1</li>
<li>torch 2.0.0 -&gt; 2.0.1</li>
<li>torchaudio 2.0.1 -&gt; 2.0.2</li>
<li>torchdata 0.6.0 -&gt; 0.6.1</li>
<li>torchtext 0.15.1 -&gt; 0.15.2</li>
<li>torchvision 0.15.1 -&gt; 0.15.2</li>
<li>tornado 6.2 -&gt; 6.3.1</li>
</ul>
</li>
</ul>
<h3>2023-05-05</h3>
<ul>
<li>Released GPU type selection for paid users, allowing them to choose a
preferred NVidia GPU</li>
<li>Upgraded R from 4.2.3 to 4.3.0</li>
<li>Upgraded Python from 3.9.16 to 3.10.11</li>
<li>Python package updates:<ul>
<li>attrs 22.2.0 -&gt; attrs 23.1.0</li>
<li>earthengine-api 0.1.349 -&gt; earthengine-api 0.1.350</li>
<li>flax 0.6.8 -&gt; 0.6.9</li>
<li>grpcio 1.53.0 -&gt; 1.54.0</li>
<li>nbclient 0.7.3 -&gt; 0.7.4</li>
<li>tensorflow-datasets 4.8.3 -&gt; 4.9.2</li>
<li>termcolor 2.2.0 -&gt; 2.3.0</li>
<li>zict 2.2.0 -&gt; 3.0.0</li>
</ul>
</li>
</ul>
<h3>2023-04-14</h3>
<ul>
<li>Python package updates:<ul>
<li>google-api-python-client 2.70.0 -&gt; 2.84.0</li>
<li>google-auth-oauthlib 0.4.6 -&gt; 1.0.0</li>
<li>google-cloud-bigquery 3.4.2 -&gt; 3.9.0</li>
<li>google-cloud-datastore 2.11.1 -&gt; 2.15.1</li>
<li>google-cloud-firestore 2.7.3 -&gt; 2.11.0</li>
<li>google-cloud-language 2.6.1 -&gt; 2.9.1</li>
<li>google-cloud-storage 2.7.0 -&gt; 2.8.0</li>
<li>google-cloud-translate 3.8.4 -&gt; 3.11.1</li>
<li>networkx 3.0 -&gt; 3.1</li>
<li>notebook 6.3.0 -&gt; 6.4.8</li>
<li>jax 0.4.7 -&gt; 0.4.8</li>
<li>pandas 1.4.4 -&gt; 1.5.3</li>
<li>spacy 3.5.1 -&gt; 3.5.2</li>
<li>SQLAlchemy 1.4.47 -&gt; 2.0.9</li>
<li>xgboost 1.7.4 -&gt; 1.7.5</li>
</ul>
</li>
</ul>
<h3>2023-03-31</h3>
<ul>
<li>Improve bash ! syntax highlighting
(<a href="https://github.com/googlecolab/colabtools/issues/3507" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Fix bug where VIM keybindings weren't working in the file editor</li>
<li>Upgraded R from 4.2.2 to 4.2.3</li>
<li>Python package updates:<ul>
<li>arviz 0.12.1 --&gt; 0.15.1</li>
<li>astropy 4.3.1 --&gt; 5.2.2</li>
<li>dopamine-rl 1.0.5 --&gt; 4.0.6</li>
<li>gensim 3.6.0 --&gt; 4.3.1</li>
<li>ipykernel 5.3.4 -&gt; 5.5.6</li>
<li>ipython 7.9.0 -&gt; 7.34.0</li>
<li>jax 0.4.4 -&gt; 0.4.7</li>
<li>jaxlib 0.4.4 -&gt; 0.4.7</li>
<li>jupyter_core 5.2.0 -&gt; 5.3.0</li>
<li>keras 2.11.0 -&gt; 2.12.0</li>
<li>lightgbm 2.2.3 -&gt; 3.3.5</li>
<li>matplotlib 3.5.3 -&gt; 3.7.1</li>
<li>nltk 3.7 -&gt; 3.8.1</li>
<li>opencv-python 4.6.0.66 -&gt; 4.7.0.72</li>
<li>plotly 5.5.0 -&gt; 5.13.1</li>
<li>pymc 4.1.4 -&gt; 5.1.2</li>
<li>seaborn 0.11.2 -&gt; 0.12.2</li>
<li>spacy 3.4.4 -&gt; 3.5.1</li>
<li>sympy 1.7.1 -&gt; 1.11.1</li>
<li>tensorboard 2.11.2 -&gt; 2.12.0</li>
<li>tensorflow 2.11.0 -&gt; 2.12.0</li>
<li>tensorflow-estimator 2.11.0 -&gt; 2.12.0</li>
<li>tensorflow-hub 0.12.0 -&gt; 0.13.0</li>
<li>torch 1.13.1 -&gt; 2.0.0</li>
<li>torchaudio 0.13.1 -&gt; 2.0.1</li>
<li>torchtext 0.14.1 -&gt; 0.15.1</li>
<li>torchvision 0.14.1 -&gt; 0.15.1</li>
</ul>
</li>
</ul>
<h3>2023-03-10</h3>
<ul>
<li>Added the
<a href="https://colab.research.google.com/notebooks/editor_shortcuts.ipynb" target="_blank" rel="nofollow" aria-label="Colab editor shortcuts Link will open in a new tab">Colab editor shortcuts</a>
example notebook</li>
<li>Fixed triggering of @-mention and email autocomplete for large comments
(<a href="https://github.com/googlecolab/colabtools/issues/3383" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Added View Resources to the Runtime menu</li>
<li>Made file viewer images fit the view by default, resizing to original size
on click</li>
<li>When in VIM mode, enable copy as well as allowing propagation to monaco-vim
to escape visual mode
(<a href="https://github.com/googlecolab/colabtools/issues/3414" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Upgraded CUDA 11.6.2 -&gt; 11.8.0 and cuDNN 8.4.0.27 -&gt; 8.7.0.84</li>
<li>Upgraded Nvidia drivers 525.78.01 -&gt; 530.30.02</li>
<li>Upgraded Python 3.8.10 -&gt; 3.9.16</li>
<li>Python package updates:<ul>
<li>beautifulsoup4 4.6.3 -&gt; 4.9.3</li>
<li>bokeh 2.3.3 -&gt; 2.4.3</li>
<li>debugpy 1.0.0 -&gt; 1.6.6</li>
<li>Flask 1.1.4 -&gt; 2.2.3</li>
<li>jax 0.3.25 -&gt; 0.4.4</li>
<li>jaxlib 0.3.25 -&gt; 0.4.4</li>
<li>Jinja2 2.11.3 -&gt; 3.1.2</li>
<li>matplotlib 3.2.2 -&gt; 3.5.3</li>
<li>nbconvert 5.6.1 -&gt; 6.5.4</li>
<li>pandas 1.3.5 -&gt; 1.4.4</li>
<li>pandas-datareader 0.9.0 -&gt; 0.10.0</li>
<li>pandas-profiling 1.4.1 -&gt; 3.2.0</li>
<li>Pillow 7.1.2 -&gt; 8.4.0</li>
<li>plotnine 0.8.0 -&gt; 0.10.1</li>
<li>scikit-image 0.18.3 -&gt; 0.19.3</li>
<li>scikit-learn 1.0.2 -&gt; 1.2.2</li>
<li>scipy 1.7.3 -&gt; 1.10.1</li>
<li>setuptools 57.4.0 -&gt; 63.4.3</li>
<li>sklearn-pandas 1.8.0 -&gt; 2.2.0</li>
<li>statsmodels 0.12.2 -&gt; 0.13.5</li>
<li>urllib3 1.24.3 -&gt; 1.26.14</li>
<li>Werkzeug 1.0.1 -&gt; 2.2.3</li>
<li>wrapt 1.14.1 -&gt; 1.15.0</li>
<li>xgboost 0.90 -&gt; 1.7.4</li>
<li>xlrd 1.2.0 -&gt; 2.0.1</li>
</ul>
</li>
</ul>
<h3>2023-02-17</h3>
<ul>
<li>Show graphs of RAM and disk usage in notebook toolbar</li>
<li>Copy cell links directly to the clipboard instead of showing a dialog when
clicking on the link icon in the cell toolbar</li>
<li>Updated the
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Fmarketplace.html" target="_blank" rel="nofollow" aria-label="Colab Marketplace VM image Link will open in a new tab">Colab Marketplace VM image</a></li>
<li>Upgraded CUDA to 11.6.2 and cuDNN to 8.4.0.27</li>
<li>Python package updates:<ul>
<li>tensorflow 2.9.2 -&gt; 2.11.0</li>
<li>tensorboard 2.9.1 -&gt; 2.11.2</li>
<li>keras 2.9.0 -&gt; 2.11.0</li>
<li>tensorflow-estimator 2.9.0 -&gt; 2.11.0</li>
<li>tensorflow-probability 0.17.0 -&gt; 0.19.0</li>
<li>tensorflow-gcs-config 2.9.0 -&gt; 2.11.0</li>
<li>earthengine-api 0.1.339 -&gt; 0.1.341</li>
<li>flatbuffers 1.12 -&gt; 23.1.21</li>
<li>platformdirs 2.6.2 -&gt; 3.0.0</li>
<li>pydata-google-auth 1.6.0 -&gt; 1.7.0</li>
<li>python-utils 3.4.5 -&gt; 3.5.2</li>
<li>tenacity 8.1.0 -&gt; 8.2.1</li>
<li>tifffile 2023.1.23.1 -&gt; 2023.2.3</li>
<li>notebook 5.7.16 -&gt; 6.3.0</li>
<li>tornado 6.0.4 -&gt; 6.2</li>
<li>aiohttp 3.8.3 -&gt; 3.8.4</li>
<li>charset-normalizer 2.1.1 -&gt; 3.0.1</li>
<li>fastai 2.7.0 -&gt; 2.7.1</li>
<li>soundfile 0.11.0 -&gt; 0.12.1</li>
<li>typing-extensions 4.4.0 -&gt; 4.5.0</li>
<li>widgetsnbextension 3.6.1 -&gt; 3.6.2</li>
<li>pydantic 1.10.4 -&gt; 1.10.5</li>
<li>zipp 3.12.0 -&gt; 3.13.0</li>
<li>numpy 1.21.6 -&gt; 1.22.4</li>
<li>drivefs 66.0 -&gt; 69.0</li>
<li>gdal 3.0.4 -&gt; 3.3.2
<a href="https://github.com/googlecolab/colabtools/issues/3375" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a></li>
</ul>
</li>
<li>Added libudunits2-dev for smoother R package installs
<a href="https://github.com/googlecolab/colabtools/issues/2831" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a></li>
</ul>
<h3>2023-02-03</h3>
<ul>
<li>Improved tooltips for pandas series to show common statistics about the
series object</li>
<li>Made the forms dropdown behave like an autocomplete box when it allows input</li>
<li>Updated the nvidia driver from 460.32.03 to 510.47.03</li>
<li>Python package updates:<ul>
<li>absl-py 1.3.0 -&gt; 1.4.0</li>
<li>bleach 5.0.1 -&gt; 6.0.0</li>
<li>cachetools 5.2.1 -&gt; 5.3.0</li>
<li>cmdstanpy 1.0.8 -&gt; 1.1.0</li>
<li>dnspython 2.2.1 -&gt; 2.3.0</li>
<li>fsspec 2022.11.0 -&gt; 2023.1.0</li>
<li>google-cloud-bigquery-storage 2.17.0 -&gt; 2.18.1</li>
<li>holidays 0.18 -&gt; 0.19</li>
<li>jupyter-core 5.1.3 -&gt; 5.2.0</li>
<li>packaging 21.3 -&gt; 23.0</li>
<li>prometheus-client 0.15.0 -&gt; 0.16.0</li>
<li>pyct 0.4.8 -&gt; 0.5.0</li>
<li>pydata-google-auth 1.5.0 -&gt; 1.6.0</li>
<li>python-slugify 7.0.0 -&gt; 8.0.0</li>
<li>sqlalchemy 1.4.46 -&gt; 2.0.0</li>
<li>tensorflow-io-gcs-filesystem 0.29.0 -&gt; 0.30.0</li>
<li>tifffile 2022.10.10 -&gt; 2023.1.23.1</li>
<li>zipp 3.11.0 -&gt; 3.12.0</li>
<li>Pinned sqlalchemy to version 1.4.46</li>
</ul>
</li>
</ul>
<h3>2023-01-12</h3>
<ul>
<li>Added support for @-mention and email autocomplete in comments</li>
<li>Improved errors when GitHub notebooks can't be loaded</li>
<li>Increased color contrast for colors used for syntax highlighting in the code
editor</li>
<li>Added terminal access for custom GCE VM runtimes</li>
<li>Upgraded Ubuntu from 18.04 LTS to 20.04 LTS
(<a>GitHub issue</a>)</li>
<li>Python package updates:<ul>
<li>GDAL 2.2.2 -&gt; 2.2.3.</li>
<li>NumPy from 1.21.5 to 1.21.6.</li>
<li>attrs 22.1.0 -&gt; 22.2.0</li>
<li>chardet 3.0.4 -&gt; 4.0.0</li>
<li>cloudpickle 1.6.0 -&gt; 2.2.0</li>
<li>filelock 3.8.2 -&gt; 3.9.0</li>
<li>google-api-core 2.8.2 -&gt; 2.11.0</li>
<li>google-api-python-client 1.12.11 -&gt; 2.70.0</li>
<li>google-auth-httplib2 0.0.3 -&gt; 0.1.0</li>
<li>google-cloud-bigquery 3.3.5 -&gt; 3.4.1</li>
<li>google-cloud-datastore 2.9.0 -&gt; 2.11.0</li>
<li>google-cloud-firestore 2.7.2 -&gt; 2.7.3</li>
<li>google-cloud-storage 2.5.0 -&gt; 2.7.0</li>
<li>holidays 0.17.2 -&gt; holidays 0.18</li>
<li>importlib-metadata 5.2.0 -&gt; 6.0.0</li>
<li>networkx 2.8.8 -&gt; 3.0</li>
<li>opencv-python-headless 4.6.0.66 -&gt; 4.7.0.68</li>
<li>pip 21.1.3 -&gt; 22.04</li>
<li>pip-tools 6.2.0 -&gt; 6.6.2</li>
<li>prettytable 3.5.0 -&gt; 3.6.0</li>
<li>requests 2.23.0 -&gt; 2.25.1</li>
<li>termcolor 2.1.1 -&gt; 2.2.0</li>
<li>torch 1.13.0 -&gt; 1.13.1</li>
<li>torchaudio 0.13.0 -&gt; 0.13.1</li>
<li>torchtext 0.14.0-&gt; 0.14.1</li>
<li>torchvision 0.14.0 -&gt; 0.14.1</li>
</ul>
</li>
</ul>
<h3>2022-12-06</h3>
<ul>
<li>Made fallback runtime version available until mid-December
(<a href="https://github.com/googlecolab/colabtools/issues/3246" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Upgraded to Python 3.8
(<a href="https://github.com/googlecolab/colabtools/issues/3246" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Python package updates:<ul>
<li>jax from 0.3.23 to 0.3.25, jaxlib from 0.3.22 to 0.3.25</li>
<li>pyarrow from 6.0.1 to 9.0.0</li>
<li>torch from 1.12.1 to 1.13.0</li>
<li>torchaudio from 0.12.1 to 0.13.0</li>
<li>torchvision from 0.13.1 to 0.14.0</li>
<li>torchtext from 0.13.1 to 0.14.0</li>
<li>xlrd from 1.1.0 to 1.2.0</li>
<li>DriveFS from 62.0.1 to 66.0.3</li>
</ul>
</li>
<li>Made styling of markdown tables in outputs match markdown tables in text
cells</li>
<li>Improved formatting for empty interactive table rows</li>
<li>Fixed syntax highlighting for variables with names that contain Python
keywords
(<a href="https://github.com/googlecolab/colabtools/issues/3210" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
</ul>
<h3>2022-11-11</h3>
<ul>
<li>Added more dark editor themes for Monaco (when in dark mode, "Editor
colorization" appears as an option in the Editor tab of the Tools → Settings
dialog)</li>
<li>Fixed bug where collapsed forms were deleted on mobile
<a href="https://github.com/googlecolab/colabtools/issues/3153" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a></li>
<li>Python package updates:<ul>
<li>rpy2 from 3.4.0 to 3.5.5
(<a href="https://github.com/googlecolab/colabtools/issues/3180" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>notebook from 5.5.0 to 5.7.16</li>
<li>tornado from 5.1.1 to 6.0.4</li>
<li>tensorflow_probability from 0.16.0 to 0.17.0</li>
<li>pandas-gbq from 0.13.3 to 0.17.9</li>
<li>protobuf from 3.17.3 to 3.19.6</li>
<li>google-api-core[grpc] from 1.31.5 to 2.8.2</li>
<li>google-cloud-bigquery from 1.21.0 to 3.3.5</li>
<li>google-cloud-core from 1.0.1 to 2.3.2</li>
<li>google-cloud-datastore from 1.8.0 to 2.9.0</li>
<li>google-cloud-firestore from 1.7.0 to 2.7.2</li>
<li>google-cloud-language from 1.2.0 to 2.6.1</li>
<li>google-cloud-storage from 1.18.0 to 2.5.0</li>
<li>google-cloud-translate from 1.5.0 to 3.8.4</li>
</ul>
</li>
</ul>
<h3>2022-10-21</h3>
<ul>
<li>Launched a single-click way to get from BigQuery to Colab to further explore
query results
(<a href="https://www.google.com/url?q=https%3A%2F%2Fcloud.google.com%2Fbigquery%2Fdocs%2Fexplore-data-colab" target="_blank" rel="nofollow" aria-label="announcement Link will open in a new tab">announcement</a>)</li>
<li>Launched
<a href="https://colab.research.google.com/signup" target="_blank" rel="nofollow" aria-label="Pro, Pro+, and Pay As You Go Link will open in a new tab">Pro, Pro+, and Pay As You Go</a> to
19 additional countries: Austria, Belgium, Bulgaria, Croatia, Cyprus,
Czechia, Denmark, Estonia, Finland, Greece, Hungary, Latvia, Lithuania,
Norway, Portugal, Romania, Slovakia, Slovenia, and Sweden
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1579956393834344449" target="_blank" rel="nofollow" aria-label="tweet Link will open in a new tab">tweet</a>)</li>
<li>Updated jax from 0.3.17 to 0.3.23, jaxlib from 0.3.15 to 0.3.22, TensorFlow
from 2.8.2 to 2.9.2, CUDA from 11.1 to 11.2, and cuDNN from 8.0 to 8.1
(<a href="https://github.com/googlecolab/backend-info" target="_blank" rel="nofollow" aria-label="backend-info Link will open in a new tab">backend-info</a>)</li>
<li>Added a <code>readonly</code> option to
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/drive.py#L99" target="_blank" rel="nofollow" aria-label="drive.mount Link will open in a new tab"><code>drive.mount</code></a></li>
<li>Fixed bug where Xarray was not working
(<a href="https://github.com/googlecolab/colabtools/issues/3134" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Modified Markdown parsing to ignore block quote symbol within MathJax
(<a href="https://github.com/googlecolab/colabtools/issues/3118" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
</ul>
<h3>2022-09-30</h3>
<ul>
<li>Launched <a href="https://colab.research.google.com/signup" target="_blank" rel="nofollow" aria-label="Pay As You Go Link will open in a new tab">Pay As You Go</a>, allowing
premium GPU access without requiring a subscription</li>
<li>Added vim and tcllib to our runtime image</li>
<li>Fixed bug where open files were closed on kernel disconnect
(<a href="https://github.com/googlecolab/colabtools/issues/1716" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Fixed bug where the play button/execution indicator was not clickable when
scrolled into the cell output
(<a href="https://github.com/googlecolab/colabtools/issues/3068" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Updated the styling for form titles so that they avoid obscuring the code
editor</li>
<li>Created a GitHub repo,
<a href="https://github.com/googlecolab/backend-info" target="_blank" rel="nofollow" aria-label="backend-info Link will open in a new tab">backend-info</a>, with the latest
apt-list.txt and pip-freeze.txt files for the Colab runtime
(<a href="https://github.com/googlecolab/colabtools/issues/1445" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Added
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/files.py#L33" target="_blank" rel="nofollow" aria-label="files.upload_file(filename) Link will open in a new tab"><code>files.upload_file(filename)</code></a>
to upload a file from the browser to the runtime with a specified filename</li>
</ul>
<h3>2022-09-16</h3>
<ul>
<li>Upgraded pymc from 3.11.0 to 4.1.4, jax from 0.3.14 to 0.3.17, jaxlib from
0.3.14 to 0.3.15, fsspec from 2022.8.1 to 2022.8.2</li>
<li>Modified our save flow to avoid persisting Drive filenames as titles in
notebook JSON</li>
<li>Updated our <a href="https://colab.research.google.com/pro/terms" target="_blank" rel="nofollow" aria-label="Terms of Service Link will open in a new tab">Terms of Service</a></li>
<li>Modified the <code>Jump to Cell</code> command to locate the cursor at the end of the
command palette input (<code>Jump to cell</code> in Tools → Command palette in a
notebook with section headings)</li>
<li>Updated the styling of the Drive notebook comment UI</li>
<li>Added support for terminating your runtime from code: <code>python from google.colab import runtime runtime.unassign()</code></li>
<li>Added regex filter support to the Recent notebooks dialog</li>
<li>Inline google.colab.files.upload JS to fix <code>files.upload()</code> not working
(<a href="https://github.com/googlecolab/colabtools/issues/51" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
</ul>
<h3>2022-08-26</h3>
<ul>
<li>Upgraded PyYAML from 3.13 to 6.0
(<a href="https://github.com/googlecolab/colabtools/issues/2942" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>),
drivefs from 61.0.3 to 62.0.1</li>
<li>Upgraded TensorFlow from 2.8.2 to 2.9.1 and ipywidgets from 7.7.1 to 8.0.1
but rolled both back due to a number of user reports
(<a href="https://github.com/googlecolab/colabtools/issues/3008" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>,
<a href="https://github.com/googlecolab/colabtools/issues/3020#issuecomment-1223330253" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Stop persisting inferred titles in notebook JSON
(<a href="https://github.com/googlecolab/colabtools/issues/764" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Fix bug in background execution which affected some Pro+ users
(<a href="https://github.com/googlecolab/colabtools/issues/2991" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Fix bug where <code>Download as .py</code> incorrectly handled text cells ending in a
double quote</li>
<li>Fix bug for Pro and Pro+ users where we weren't honoring the preference
(Tools → Settings) to use a temporary scratch notebook as the default
landing page</li>
<li>Provide undo/redo for scratch cells</li>
<li>When writing ipynb files, serialize empty multiline strings as <code>[]</code> for
better consistency with JupyterLab</li>
</ul>
<h3>2022-08-11</h3>
<ul>
<li>Upgraded ipython from 5.5.0 to 7.9.0, fbprophet 0.7 to prophet 1.1,
tensorflow-datasets from 4.0.1 to 4.6.0, drivefs from 60.0.2 to 61.0.3,
pytorch from 1.12.0 to 1.12.1, numba from 0.51 to 0.56, and lxml from 4.2.0
to 4.9.1</li>
<li>Loosened our <code>requests</code> version requirement
(<a href="https://github.com/deepset-ai/haystack/pull/2921#issuecomment-1199714337" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Removed support for TensorFlow 1</li>
<li>Added Help → Report Drive abuse for Drive notebooks</li>
<li>Fixed indentation for Python lines ending in <code>[</code></li>
<li>Modified styling of tables in Markdown to left-align them rather than
centering them</li>
<li>Fixed special character replacement when copying interactive tables as
Markdown</li>
<li>Fixed ansi 8-bit color parsing
(<a href="https://github.com/googlecolab/colabtools/issues/2963" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Configured logging to preempt transitive imports and other loading from
implicitly configuring the root logger</li>
<li>Modified forms to use a value of <code>None</code> instead of causing a parse error
when clearing raw and numeric-typed form fields</li>
</ul>
<h3>2022-07-22</h3>
<ul>
<li>Update scipy from 1.4.1 to 1.7.3, drivefs from 59.0.3 to 60.0.2, pytorch
from 1.11 to 1.12, jax &amp; jaxlib from 0.3.8 to 0.3.14, opencv-python from
4.1.2.30 to 4.6.0.66, spaCy from 3.3.1 to 3.4.0, and dlib from 19.18.0 to
19.24.0</li>
<li>Fix <code>Open in tab</code> doc link which was rendering incorrectly
(<a href="https://github.com/googlecolab/colabtools/issues/2690" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>)</li>
<li>Add a preference for the default tab orientation to the Site section of the
settings menu under Tools → Settings</li>
<li>Show a warning for <code>USE_AUTH_EPHEM</code> usage when running authenticate_user on
a TPU runtime
(<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/auth.py#L243" target="_blank" rel="nofollow" aria-label="code Link will open in a new tab">code</a>)</li>
</ul>
<h3>2022-07-01</h3>
<ul>
<li>Add a preference for code font to the settings menu under Tools → Settings</li>
<li>Update drivefs from 58.0.3 to 59.0.3 and spacy from 2.2.4 to 3.3.1</li>
<li>Allow
<a href="https://www.google.com/url?q=https%3A%2F%2Fipython.org%2Fipython-doc%2F3%2Fnotebook%2Fnbformat.html%23display-data" target="_blank" rel="nofollow" aria-label="display_data Link will open in a new tab">display_data</a>
and
<a href="https://www.google.com/url?q=https%3A%2F%2Fipython.org%2Fipython-doc%2F3%2Fnotebook%2Fnbformat.html%23execute-result" target="_blank" rel="nofollow" aria-label="execute_result Link will open in a new tab">execute_result</a>
text outputs to wrap, matching behavior of JupyterLab (does not affect
stream outputs/print statements).</li>
<li>Improve LSP handling of some magics, esp. %%writefile
(<a href="https://github.com/googlecolab/colabtools/issues/2859" target="_blank" rel="nofollow" aria-label="GitHub issue Link will open in a new tab">GitHub issue</a>).</li>
<li>Add a
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Ffaq.html%23drive-mount-code-cell" target="_blank" rel="nofollow" aria-label="FAQ entry Link will open in a new tab">FAQ entry</a>
about the mount Drive button behavior and include link buttons for each FAQ
entry.</li>
<li>Fix bug where the notebook was sometimes hidden behind other tabs on load
when in single pane view.</li>
<li>Fix issue with inconsistent scrolling when an editor is in multi-select
mode.</li>
<li>Fix bug where clicking on a link in a form would navigate away from the
notebook</li>
<li>Show a confirmation dialog before performing Replace all from the Find and
replace pane.</li>
</ul>
<h3>2022-06-10</h3>
<ul>
<li>Update drivefs from 57.0.5 to 58.0.3 and tensorflow from 2.8.0 to 2.8.2</li>
<li>Support more than 100 repos in the GitHub repo selector shown in the open
dialog and the clone to GitHub dialog</li>
<li>Show full notebook names on hover in the open dialog</li>
<li>Improve the color contrast for links, buttons, and the
<code>ipywidgets.Accordion</code> widget in dark mode</li>
</ul>
<h3>2022-05-20</h3>
<ul>
<li>Support URL params for linking to some common pref settings:
<a href="https://colab.research.google.com/?force_theme=dark" target="_blank" rel="nofollow" aria-label="force_theme=dark Link will open in a new tab">force_theme=dark</a>,
<a href="https://colab.research.google.com/?force_corgi_mode=1" target="_blank" rel="nofollow" aria-label="force_corgi_mode=1 Link will open in a new tab">force_corgi_mode=1</a>,
<a href="https://colab.research.google.com/?force_font_size=14" target="_blank" rel="nofollow" aria-label="force_font_size=14 Link will open in a new tab">force_font_size=14</a>.
Params forced by URL are not persisted unless saved using Tools → Settings.</li>
<li>Add a class <code>markdown-google-sans</code> to allow
<span class="markdown-google-sans">Markdown to render in Google Sans</span></li>
<li>Update monaco-vim from 0.1.19 to 0.3.4</li>
<li>Update drivefs from 55.0.3 to 57.0.5, jax from 0.3.4 to 0.3.8, and jaxlib
from 0.3.2 to 0.3.7</li>
</ul>
<h3>2022-04-29</h3>
<ul>
<li>Added 🦀 mode (under Miscellaneous in Tools → Settings)</li>
<li>Added "Disconnect and delete runtime" option to the menu next to the Connect
button</li>
<li>Improved rendering of filter options in an interactive table</li>
<li>Added git-lfs to the base image</li>
<li>Updated torch from 1.10.0 to 1.11.0, jupyter-core from 4.9.2 to 4.10.0, and
cmake from 3.12.0 to 3.22.3</li>
<li>Added more details to our
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Ffaq.html" target="_blank" rel="nofollow" aria-label="FAQ Link will open in a new tab">FAQ</a> about unsupported
uses (using proxies, downloading torrents, etc.)</li>
<li>Fixed <a href="https://github.com/googlecolab/colabtools/issues/2779" target="_blank" rel="nofollow" aria-label="issue Link will open in a new tab">issue</a> with
apt-get dependencies</li>
</ul>
<h3>2022-04-15</h3>
<ul>
<li>Add an option in the file browser to show hidden files.</li>
<li>Upgrade gdown from 4.2.0 to 4.4.0, google-api-core[grpc] from 1.26.0 to
1.31.5, and pytz from 2018.4 to 2022.1</li>
</ul>
<h3>2022-03-25</h3>
<ul>
<li>Launched
<a href="https://colab.research.google.com/signup?utm_source=relnotes&amp;utm_medium=link&amp;utm_campaign=additional_countries" target="_blank" rel="nofollow" aria-label="Pro/Pro+ Link will open in a new tab">Pro/Pro+</a>
to 12 additional countries: Australia, Bangladesh, Colombia, Hong Kong,
Indonesia, Mexico, New Zealand, Pakistan, Philippines, Singapore, Taiwan,
and Vietnam</li>
<li>Added
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/auth.py#L253" target="_blank" rel="nofollow" aria-label="google.colab.auth.authenticate_service_account() Link will open in a new tab"><code>google.colab.auth.authenticate_service_account()</code></a>
to support using
<a href="https://www.google.com/url?q=https%3A%2F%2Fcloud.google.com%2Fiam%2Fdocs%2Fcreating-managing-service-account-keys%23iam-service-account-keys-create-console" target="_blank" rel="nofollow" aria-label="Service Account keys Link will open in a new tab">Service Account keys</a></li>
<li>Update jax from 0.3.1 to 0.3.4 &amp; jaxlib from 0.3.0 to 0.3.2</li>
<li>Fixed an issue with Twitter previews of notebooks shared as GitHub Gists</li>
</ul>
<h3>2022-03-10</h3>
<ul>
<li>Launched
<a href="https://colab.research.google.com/signup?utm_source=relnotes&amp;utm_medium=link&amp;utm_campaign=additional_countries" target="_blank" rel="nofollow" aria-label="Pro/Pro+ Link will open in a new tab">Pro/Pro+</a>
to 10 new countries: Ireland, Israel, Italy, Morocco, the Netherlands,
Poland, Spain, Switzerland, Turkey, and the United Arab Emirates</li>
<li>Launched support for
<a href="https://github.com/googlecolab/colabtools/wiki/Scheduled-notebooks" target="_blank" rel="nofollow" aria-label="scheduling notebooks for Pro+ users Link will open in a new tab">scheduling notebooks for Pro+ users</a></li>
<li>Fixed bug in interactive datatables where filtering by number did not work</li>
<li>Finished removing the python2 kernelspec</li>
</ul>
<h3>2022-02-25</h3>
<ul>
<li>Made various accessibility improvements to the header</li>
<li>Fix bug with
<a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fnotebooks%2Fforms.ipynb%23scrollTo%3Dh9aZYKhly2h_" target="_blank" rel="nofollow" aria-label="forms run:auto Link will open in a new tab">forms run:auto</a>
where a form field change would trigger multiple runs</li>
<li>Minor updates to the
<a href="https://colab.research.google.com/notebooks/bigquery.ipynb" target="_blank" rel="nofollow" aria-label="bigquery example notebook Link will open in a new tab">bigquery example notebook</a>
and snippet</li>
<li>Include background execution setting in the sessions dialog for Pro+ users</li>
<li>Update tensorflow-probability from 0.15 to 0.16</li>
<li>Update jax from 0.2.25 to 0.3.1 &amp; jaxlib from 0.1.71 to 0.3.0</li>
</ul>
<h3>2022-02-11</h3>
<ul>
<li>Improve keyboard navigation for the open dialog</li>
<li>Fix issue where nvidia-smi stopped reporting resource utilization for some
users who were modifying the version of nvidia used</li>
<li>Update tensorflow from 2.7 to 2.8, keras from 2.7 to 2.8, numpy from 1.19.5
to 1.21.5, tables from 3.4.4 to 3.7.0</li>
</ul>
<h3>2022-02-04</h3>
<ul>
<li>Improve UX for opening content alongside your notebook, such as files opened
from the file browser. This includes a multi-pane view and drag-drop support</li>
<li>Better Twitter previews when sharing example Colab notebooks and notebooks
opened from GitHub Gists</li>
<li>Update pandas from 1.1.5 to 1.3.5</li>
<li>Update openpyxl from 2.5.9 to 3.0.0 and pyarrow from 3.0.0 to 6.0.0</li>
<li>Link to the release notes from the Help menu</li>
</ul>
<h3>2022-01-28</h3>
<ul>
<li>Add a copy button to
<a href="https://colab.research.google.com/notebooks/data_table.ipynb" target="_blank" rel="nofollow" aria-label="data tables Link will open in a new tab">data tables</a></li>
<li>Python LSP support for better completions and code diagnostics. This can be
configured in the Editor Settings (Tools → Settings)</li>
<li>Update
<a href="https://colab.research.google.com/notebooks/io.ipynb#scrollTo=sOm9PFrT8mGG" target="_blank" rel="nofollow" aria-label="gspread examples Link will open in a new tab">gspread examples</a>
in our documentation</li>
<li>Update gdown from 3.6 to 4.2</li>
</ul>
<h3>2022-01-21</h3>
<ul>
<li>New documentation for the
<a href="https://colab.research.google.com/notebooks/google.colab.ipynb" target="_blank" rel="nofollow" aria-label="google.colab package Link will open in a new tab"><code>google.colab</code> package</a></li>
<li>Show GPU RAM in the resource usage tab</li>
<li>Improved security for mounting Google Drive which disallows mounting Drive
from accounts other than the one currently executing the notebook</li>
</ul>
<h3>2022-01-14</h3>
<ul>
<li>Add a preference (Tools → Settings) to use a temporary scratch notebook as
the default landing page</li>
<li>Fix bug where <code>/</code> and <code>:</code> weren't working in VIM mode</li>
<li>Update gspread from 3.0 to 3.4</li>
<li>Update the
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Fmarketplace.html" target="_blank" rel="nofollow" aria-label="Colab Marketplace VM image Link will open in a new tab">Colab Marketplace VM image</a></li>
</ul></span></div></colab-scroller></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$739266375$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$739266375$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$739266375$--><md-icon-button id="tab-pane-3-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./train_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./train_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowrootmode="open"><!---->
      <md-icon-button toggle="" id="toggle-composer-button" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$739266375$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$739266375$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$739266375$--><span class="icon"><slot></slot></span>
        <!--?lit$739266375$-->
        <!--?lit$739266375$--><span class="touch"></span>
  </button></template>
        <!--?lit$739266375$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer-button" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="right">
        <!--?lit$739266375$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template><!--?lit$739266375$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon><!--?lit$739266375$-->2:53 PM</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Focus the last run cell

2:53 PM (0 minutes ago)
executed in 2.981s"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Focus the last run cell</div><!----><!----><br><!----><!----><div><!--?lit$739266375$-->2:53 PM (0 minutes ago)</div><!----><!----><div><!--?lit$739266375$-->executed in 2.981s</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$739266375$--><!--?lit$739266375$--><!--?lit$739266375$--><colab-runtime-status><template shadowrootmode="open"><!----><md-text-button data-aria-expanded="false" data-aria-haspopup="menu" id="runtime-options" aria-describedby="runtime-options-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button" aria-haspopup="menu" aria-expanded="false">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dns</md-icon><!--?lit$739266375$-->Python 3</md-text-button><colab-tooltip-trigger aria-hidden="true" for="runtime-options" id="runtime-options-tooltip" message="Runtime options"><template shadowrootmode="open"><!----><!--?lit$739266375$--><!----><div><!--?lit$739266375$-->Runtime options</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->data_object</md-icon>
        <!--?lit$739266375$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$739266375$-->terminal</md-icon>
        <!--?lit$739266375$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 70px; top: 62px; display: none;"><!--?lit$739266375$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Locate in Drive<!--?lit$739266375$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Open in playground mode<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->New notebook in Drive<!--?lit$739266375$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Open notebook<!--?lit$739266375$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="search-notebooks-in-drive" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Search notebooks in Drive<!--?lit$739266375$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$739266375$-->(opens in a new tab)</span></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":8" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Upload notebook<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":9" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Rename<!--?lit$739266375$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Move<!--?lit$739266375$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Move to trash<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":d" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save a copy in Drive<!--?lit$739266375$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save a copy as a GitHub Gist<!--?lit$739266375$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save a copy in GitHub<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":h" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save<!--?lit$739266375$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save and pin revision<!--?lit$739266375$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Revision history<!--?lit$739266375$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Notebook info<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":m" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$739266375$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Print<!--?lit$739266375$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Download .ipynb<!--?lit$739266375$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Download .py<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Undo<!--?lit$739266375$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Redo<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":u" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Select all cells<!--?lit$739266375$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Cut cell or selection<!--?lit$739266375$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Copy cell or selection<!--?lit$739266375$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Paste<!--?lit$739266375$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Delete selected cells<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":10" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Find and replace<!--?lit$739266375$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":12" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Find next<!--?lit$739266375$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Find previous<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Notebook settings<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":16" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Clear all outputs<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$739266375$-->Table of contents<!--?lit$739266375$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Executed code history<!--?lit$739266375$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Start slideshow<!--?lit$739266375$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Start slideshow from beginning<!--?lit$739266375$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$739266375$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1h" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Collapse sections<!--?lit$739266375$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Expand sections<!--?lit$739266375$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Save collapsed section layout<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Show/hide code<!--?lit$739266375$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Show/hide output<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1o" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Focus next tab<!--?lit$739266375$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Focus previous tab<!--?lit$739266375$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Move tab to next pane<!--?lit$739266375$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Move tab to previous pane<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Hide comments<!--?lit$739266375$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Minimize comments<!--?lit$739266375$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Expand comments<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Code cell<!--?lit$739266375$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Text cell<!--?lit$739266375$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Section header cell<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Scratch code cell<!--?lit$739266375$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Code snippets<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":20" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Add a form field<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Run all<!--?lit$739266375$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Run before<!--?lit$739266375$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Run the focused cell<!--?lit$739266375$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Run selection<!--?lit$739266375$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Run cell and below<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":28" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Interrupt execution<!--?lit$739266375$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Restart session<!--?lit$739266375$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Restart session and run all<!--?lit$739266375$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Disconnect and delete runtime<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2d" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Change runtime type<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2f" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Manage sessions<!--?lit$739266375$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->View resources<!--?lit$739266375$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->View runtime logs<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2j" style="user-select: none;"></div><div command="deploy-cloud-run" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Deploy to Google Cloud Run<!--?lit$739266375$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Command palette<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2n" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Settings<!--?lit$739266375$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Keyboard shortcuts<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2q" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Diff notebooks<!--?lit$739266375$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$739266375$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$739266375$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Frequently asked questions<!--?lit$739266375$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->View release notes<!--?lit$739266375$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Search code snippets<!--?lit$739266375$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2w" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Report a bug<!--?lit$739266375$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Report Drive abuse<!--?lit$739266375$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->Send feedback<!--?lit$739266375$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":30" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$739266375$-->View terms of service<!--?lit$739266375$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$739266375$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$739266375$--><button id="button" class="button">
      <!--?lit$739266375$-->
      <span class="touch"></span>
      <!--?lit$739266375$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$739266375$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$739266375$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="context-view" aria-hidden="true" style="display: none;"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxyecf66cda808c14f9b8282d755a81ba015e9b12ec0.260073596" name="apiproxyecf66cda808c14f9b8282d755a81ba015e9b12ec0.260073596" src="./train_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-c2a7logq50dj" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./train_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./train_files/saved_resource.html"></iframe></div><iframe src="./train_files/bscframe.html" style="display: none;"></iframe></body></html>