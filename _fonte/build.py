#!/usr/bin/env python3
"""Gera o site estático. Uso: python3 build.py https://www.seudominio.com.br"""
import sys,os,json,shutil
SITE=(sys.argv[1] if len(sys.argv)>1 else "https://felipegoulart.dev.br").rstrip('/')
NOME="Felipe Goulart"; WA="https://wa.me/5547991237643"; FONE="(47) 99123-7643"; MAIL="contato@felipegoulart.dev.br"
HOJE="2026-11-18"; OUT="dist"
BL="https://felipegoulart.vercel.app"
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT+"/img")
for f in os.listdir("img"): shutil.copy("img/"+f,OUT+"/img/"+f)
shutil.copy("img/favicon-aguia.jpg",OUT+"/favicon.jpg")
shutil.copy("img/favicon-aguia.png",OUT+"/favicon.png")
def wa(t): 
    from urllib.parse import quote
    return WA+"?text="+quote(t)

CSS="""
:root{--bg:#fff;--tx:#23272b;--mu:#5d646b;--ln:#d5d9dd;--so:#f4f5f6;--in:#2f343a;--on:#fff;--ac:#0b6b3a}
@media(prefers-color-scheme:dark){:root{--bg:#1d2024;--tx:#e6e8ea;--mu:#a7adb3;--ln:#41464c;--so:#272b30;--in:#e6e8ea;--on:#1d2024;--ac:#5fd397}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;touch-action:pan-x pan-y;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--tx);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;touch-action:pan-x pan-y;padding:env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left)}
img{max-width:100%;height:auto}a{color:var(--ac)}
.w{max-width:1000px;margin:0 auto;padding:0 18px}
header{border-bottom:1px solid var(--ln)}header .w{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 20px;padding-top:10px;padding-bottom:10px}
.lg{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--tx);text-decoration:none}.lg img{border-radius:8px}
nav ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 6px}nav a{display:block;padding:10px 12px;color:var(--tx);text-decoration:none;font-weight:600;font-size:15px}nav a:hover,nav a[aria-current]{color:var(--ac)}
.bc{font-size:14px;color:var(--mu);padding:12px 0 0}.bc a{color:var(--mu)}
main{padding:10px 0 40px}h1{font-size:clamp(26px,5vw,38px);line-height:1.2;margin:14px 0}h2{font-size:clamp(21px,3.5vw,27px);line-height:1.25;margin:34px 0 10px}h3{font-size:18px;margin:0 0 4px}
.lead{font-size:19px;color:var(--mu)}
.btn{display:inline-block;background:var(--ac);color:#fff;padding:13px 22px;border-radius:8px;font-weight:700;text-decoration:none;margin:6px 8px 6px 0;min-height:44px}.btn.o{background:none;color:var(--ac);border:2px solid var(--ac)}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;padding:0;list-style:none}
.c{border:1px solid var(--ln);border-radius:10px;padding:16px;background:var(--so)}.c p{margin:4px 0 0;color:var(--mu);font-size:16px}.c a{font-weight:700;text-decoration:none}
.lo{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;list-style:none;padding:0}.lo figure{margin:0;border:1px solid var(--ln);border-radius:8px;overflow:hidden}.lo figcaption{font-size:13px;padding:6px 8px;color:var(--mu)}
.tb{overflow-x:auto}table{border-collapse:collapse;width:100%}th,td{border:1px solid var(--ln);padding:8px 10px;text-align:left;vertical-align:top}th{background:var(--so)}
blockquote{margin:12px 0;padding:10px 16px;border-left:4px solid var(--ac);background:var(--so)}cite{display:block;font-size:14px;color:var(--mu)}
details{border:1px solid var(--ln);border-radius:8px;padding:10px 14px;margin:8px 0}summary{font-weight:700;cursor:pointer;min-height:24px}
footer{border-top:1px solid var(--ln);background:var(--so);font-size:15px}footer .w{padding-top:24px;padding-bottom:24px;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}footer ul{list-style:none;padding:0;margin:0}footer li a{display:inline-block;padding:4px 0}
@media(max-width:600px){body{font-size:16px}.btn{display:block;text-align:center;margin-right:0}}
a,td,li{overflow-wrap:anywhere}
.fs{display:flex;flex-wrap:wrap;align-items:center;gap:16px;margin:18px 0}.fs figure{margin:0}.fs img{display:block;border-radius:12px;border:1px solid var(--ln)}.fs .ph img{border-radius:50%;width:150px;height:150px;object-fit:cover}.fs .sp img{background:#000;width:240px}.fs figcaption{font-size:13px;color:var(--mu);padding-top:6px;text-align:center}
.bl{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}.bl li{border:1px solid var(--ln);border-radius:10px;padding:12px 14px;background:var(--so)}.bl strong{display:block}.bl span{font-size:14px;color:var(--mu)}
"""
JS="""(function(){var o={passive:false};['gesturestart','gesturechange','gestureend'].forEach(function(n){document.addEventListener(n,function(e){e.preventDefault()},o)});document.addEventListener('touchmove',function(e){if(e.touches&&e.touches.length>1)e.preventDefault()},o)})();"""
open(OUT+"/style.css","w").write(CSS.strip())
NAV=[("/","Início"),("/servicos/","Serviços"),("/sobre/","Sobre"),("/projetos/","Projetos"),("/permuta/","Permuta"),("/contato/","Contato")]
ORG={"@type":"ProfessionalService","@id":SITE+"/#negocio","name":"Felipe Goulart - Desenvolvimento de Websites & Sistemas","url":SITE+"/","image":SITE+"/img/logo-felipe-goulart.jpg","telephone":"+55-47-99123-7643","email":MAIL,
 "address":{"@type":"PostalAddress","addressLocality":"Balneário Camboriú","addressRegion":"SC","addressCountry":"BR"},"areaServed":[{"@type":"City","name":"Balneário Camboriú"},{"@type":"Country","name":"Brasil"}],
 "founder":{"@type":"Person","name":NOME,"jobTitle":"Desenvolvedor de software"}}
sitemap=[]
def page(path,title,desc,h1,body,crumbs=None,extra=None,prio="0.7"):
    url=SITE+path; crumbs=crumbs or []
    ld=[dict(ORG,**{"@context":"https://schema.org"})] if path in("/","/contato/") else []
    if crumbs:
        items=[("Início","/")]+crumbs
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(items)]})
    if extra: ld.append(extra)
    bc=""
    if crumbs: bc='<nav class="bc" aria-label="Caminho"><a href="/">Início</a>'+"".join(f' › <a href="{u}">{n}</a>' for n,u in crumbs[:-1])+f' › <span>{crumbs[-1][0]}</span></nav>'
    nav="".join(f'<li><a href="{u}"{" aria-current=\"page\"" if (path==u or (u!="/" and path.startswith(u))) else ""}>{n}</a></li>' for u,n in NAV)
    html=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b6b3a"><link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/favicon.jpg">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Felipe Goulart"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/img/felipe-smartplanet.jpg">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/style.css">
{"".join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False)+'</script>' for x in ld)}
</head><body>
<header><div class="w"><a class="lg" href="/"><img src="/img/logo-felipe-goulart.png" alt="Logotipo de Felipe Goulart" width="44" height="44">Felipe Goulart</a><nav aria-label="Principal"><ul>{nav}</ul></nav></div></header>
<main class="w">{bc}<h1>{h1}</h1>{body}</main>
<footer><div class="w"><div><strong>Felipe Goulart</strong><p>Desenvolvimento de sites, sistemas, ERP e PDV em Balneário Camboriú – SC, com atendimento em todo o Brasil.</p></div>
<div><strong>Serviços</strong><ul>{"".join(f'<li><a href="/servicos/{s[0]}/">{s[1]}</a></li>' for s in SERV)}</ul></div>
<div><strong>Contato</strong><ul><li><a href="{WA}">WhatsApp {FONE}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>Balneário Camboriú – SC</li><li><a href="{BL}" rel="noopener">felipegoulart.vercel.app</a></li></ul></div></div></footer>
<script>{JS}</script></body></html>'''
    d=OUT+path; os.makedirs(d,exist_ok=True); open(d+"index.html","w",encoding="utf-8").write(html)
    sitemap.append((url,prio))
def cta(t="Quero um orçamento"): return f'<p><a class="btn" href="{wa("Olá, Felipe! Vim pelo site e quero um orçamento.")}">{t} no WhatsApp</a></p>'

# slug, nome curto, title, description, h1, intro, itens, faqs
SERV=[
("desenvolvimento-de-sites","Desenvolvimento de sites","Desenvolvimento de Sites em Balneário Camboriú – SC","Criação de sites institucionais, lojas virtuais e landing pages em Balneário Camboriú, SC. Sites rápidos, responsivos e prontos para aparecer no Google.","Desenvolvimento de sites em Balneário Camboriú",
 "Faço sites institucionais, landing pages, lojas virtuais e plataformas sob medida. Cada site é construído para carregar rápido no celular, ter uma URL para cada página e ser encontrado no Google.",
 ["Site institucional com uma página para cada serviço","Landing page para campanhas e anúncios","Loja virtual com pedidos e meios de pagamento","Versão para celular, tablet e computador","Estrutura técnica de SEO: títulos, descrições, sitemap e dados estruturados","Hospedagem, domínio e e-mail corporativo, se você precisar"],
 [("Quanto tempo leva para fazer um site?","Depende do número de páginas e das integrações. Depois de entender o que você precisa, passo um prazo por escrito junto com o orçamento."),("O site já sai otimizado para o Google?","Sim. Cada página tem título, descrição, endereço próprio e estrutura de cabeçalhos. A posição no Google depende também de conteúdo, concorrência e do seu perfil no Google Maps.")]),
("sistemas-erp-sob-medida","Sistemas e ERP sob medida","Sistemas e ERP sob Medida em Balneário Camboriú – SC","Desenvolvimento de sistemas de gestão e ERP sob medida em Balneário Camboriú, SC: estoque, financeiro, vendas e relatórios para a sua operação.","Sistemas e ERP sob medida",
 "Desenvolvo sistemas de gestão feitos para a rotina da sua empresa. Em vez de adaptar a operação a um programa pronto, o sistema segue o seu processo: do estoque ao financeiro.",
 ["Cadastro de clientes, produtos e fornecedores","Controle de estoque e movimentações","Financeiro: contas a pagar, a receber e caixa","Vendas, orçamentos e pedidos","Relatórios por período, produto e funcionário","Acesso por login, com permissões por usuário"],
 [("Qual a diferença entre ERP pronto e sob medida?","O ERP pronto atende o que a maioria precisa. O sob medida inclui só o que a sua empresa usa e se conecta às máquinas e sistemas que você já tem."),("Atende empresas fora de Balneário Camboriú?","Sim. O desenvolvimento e o suporte são feitos à distância, para todo o Brasil.")]),
("pdv-ponto-de-venda","PDV – Ponto de venda","Sistema PDV – Ponto de Venda em Balneário Camboriú – SC","Sistema PDV sob medida com impressora térmica, leitor de código de barras, etiquetadora e nota fiscal. Balneário Camboriú – SC.","Sistema PDV (ponto de venda) sob medida",
 "O PDV registra a venda no balcão, baixa o estoque e fecha o caixa. Eu integro o sistema aos equipamentos que a loja já usa: impressora térmica, leitor de código de barras, etiquetadora e gaveta.",
 ["Venda por leitura de código de barras","Impressão de cupom não fiscal na impressora térmica","Impressão de etiquetas de produto e preço","Emissão de NF-e e NFS-e, com integração à prefeitura","Abertura e fechamento de caixa","Relatórios por operador e por período"],
 [("O PDV funciona com a minha impressora?","Na maioria dos casos, sim. A integração é feita para o modelo que você já tem. Informe a marca e o modelo no contato."),("O PDV emite nota fiscal?","Sim, NF-e e NFS-e, conforme o tipo de operação da empresa. Os requisitos fiscais são alinhados antes do desenvolvimento.")]),
("automacoes-e-integracoes","Automações e integrações","Automações e Integrações de Sistemas – Balneário Camboriú","Automação de processos, integração com APIs, impressoras, máquinas de cartão e sistemas externos, e fluxos de WhatsApp. Atendimento em todo o Brasil.","Automações e integrações entre sistemas",
 "Conecto o seu sistema a outros sistemas e equipamentos para acabar com a digitação repetida: APIs, impressoras, máquinas de cartão, mensagens automáticas e planilhas.",
 ["Integração com APIs de terceiros","Integração com impressoras e máquinas de cartão","Fluxos automáticos de mensagens no WhatsApp","Envio automático de dados entre sistemas","Webhooks e notificações","Rotinas agendadas de importação e exportação"],
 [("Que tipo de tarefa vale automatizar?","Tarefas repetidas todos os dias, como lançar o mesmo dado em dois lugares, enviar a mesma mensagem ou gerar o mesmo relatório."),("Preciso trocar meu sistema atual?","Não necessariamente. Muitas automações se conectam ao sistema que você já usa.")]),
("seo-local-google-maps","SEO local e Google Maps","SEO Local e Google Maps em Balneário Camboriú – SC","Otimização do Google Meu Negócio e SEO local para empresas de Balneário Camboriú, SC: categoria, descrição, serviços, fotos e avaliações.","SEO local e Google Maps para empresas",
 "Otimizo o perfil da sua empresa no Google Maps e as páginas do site para buscas com nome de cidade, como “contador em Balneário Camboriú”. Para busca local, o perfil do Google e o site precisam dizer a mesma coisa.",
 ["Escolha da categoria principal e das categorias secundárias","Descrição, serviços, horários e fotos do perfil","Nome, endereço e telefone iguais no perfil, no site e nos diretórios","Páginas do site por serviço e por cidade atendida","Processo para pedir avaliações a clientes reais","Acompanhamento no Google Search Console"],
 [("Em quanto tempo aparece resultado?","Ajustes no perfil podem ter efeito em semanas. Posições dependem de concorrência, distância do cliente e avaliações. Não prometo posição."),("Vocês compram avaliações?","Não. Avaliações falsas ou pagas sem aviso violam as regras do Google e podem derrubar o perfil.")]),
("suporte-de-ti","Suporte de TI e infraestrutura","Suporte de TI para Empresas em Balneário Camboriú – SC","Suporte de TI, infraestrutura, servidores, backup, e-mail corporativo e manutenção para empresas em Balneário Camboriú, SC.","Suporte de TI e infraestrutura para empresas",
 "Cuido da parte técnica para a sua empresa não parar: servidor, domínio, e-mail, backup, atualização e atendimento quando algo dá problema.",
 ["Hospedagem de sites e sistemas","Domínios e e-mails corporativos","Backups e atualizações","Monitoramento do site e do sistema","Instalação de impressoras, leitores e máquinas de cartão","Consultoria para escolher a solução e reduzir custos"],
 [("O suporte é presencial?","Atendo presencialmente em Balneário Camboriú e região e à distância para o resto do Brasil."),("Vendem equipamentos?","Indico e configuro impressoras térmicas, etiquetadoras, leitores e coletores.")]),
]
def faq(fs): return "<h2>Perguntas frequentes</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in fs)
LOGOS=[("transporte-executivo","Transporte Executivo"),("e-transporte-pro","E-Transporte.PRÓ"),("luxury-drive-experience","Luxury Drive Experience"),("transfer-turismo-floripa","Transfer & Turismo – Floripa"),("hotel-blumenau","Hotel Blumenau"),("firestep","Firestep"),("smartplanet","SmartPlanet – a Boutique do Celular"),("vestmais-mara-moda-hospitalar","Vestmais Mara – Moda Hospitalar")]
def logos(n=99): return '<ul class="lo">'+"".join(f'<li><figure><img src="/img/{s}.jpg" alt="Logotipo {t}" width="480" height="270" loading="lazy" decoding="async"><figcaption>{t}</figcaption></figure></li>' for s,t in LOGOS[:n])+'</ul>'


FELIPE_SP=f'''<div class="fs"><figure class="ph"><img src="/img/felipe-goulart.jpg" alt="Foto de Felipe Goulart, desenvolvedor da SmartPlanet" width="150" height="150" loading="lazy" decoding="async"><figcaption>Felipe Goulart</figcaption></figure><figure class="sp"><img src="/img/logo-smartplanet.jpg" alt="Logotipo SmartPlanet – a Boutique do Celular" width="240" height="153" loading="lazy" decoding="async"><figcaption>SmartPlanet – a Boutique do Celular</figcaption></figure></div>'''
BL_SITES=[("Transporte Executivo","https://www.transporteexecutivo.com","Site – crédito “Desenvolvido por Felipe Goulart” no rodapé"),("SmartPlanet – a Boutique do Celular","https://www.lojadeeletronicossaojose.com.br","Loja virtual – link “Site por Felipe Goulart” no rodapé"),("Hotel Blumenau","https://www.hotelblumenau.com.br","Site com reserva online – crédito no rodapé"),("API-Construtor.PRÓ","https://www.api-construtor.pro","Plataforma de automação – crédito do desenvolvedor"),("Firestep – Sites e CRM","https://www.firestep.cloud","Site e CRM – crédito do desenvolvedor")]
def backlinks(): return '<h2>Onde encontrar o link do Felipe</h2><p>Nos sites que desenvolvi, o crédito do desenvolvedor leva para <a href="'+BL+'" rel="noopener">felipegoulart.vercel.app</a>.</p><ul class="bl">'+"".join(f'<li><strong><a href="{u}" rel="noopener">{n}</a></strong><span>{d} → <a href="{BL}" rel="noopener">felipegoulart.vercel.app</a></span></li>' for n,u,d in BL_SITES)+'</ul>'

# HOME
cards="".join(f'<li class="c"><h3><a href="/servicos/{s[0]}/">{s[1]}</a></h3><p>{s[5].split(".")[0]}.</p></li>' for s in SERV)
page("/","Sites, Sistemas e PDV em Balneário Camboriú – Felipe Goulart","Desenvolvimento de sites, sistemas sob medida, ERP, PDV, automações e suporte de TI em Balneário Camboriú – SC. Atendimento em todo o Brasil.",
 "Desenvolvimento de sites, sistemas, ERP e PDV em Balneário Camboriú – SC",
 f'''<p class="lead">Sou Felipe Goulart, desenvolvedor de software em Balneário Camboriú – SC. Crio sites, sistemas de gestão (ERP), PDV e automações sob medida para empresas, e presto suporte de TI. Atendo em todo o Brasil.</p>{cta()}
<h2>Serviços</h2><ul class="g">{cards}</ul>
<h2>Por que sistema sob medida</h2><div class="tb"><table><tr><th></th><th>Sistema genérico</th><th>Sistema sob medida</th></tr><tr><td>Equipamentos</td><td>Só funciona com a lista de máquinas compatíveis.</td><td>Integração feita para a máquina que você já tem.</td></tr><tr><td>Processo</td><td>Você adapta a empresa ao sistema.</td><td>O sistema segue o seu processo.</td></tr><tr><td>Nota fiscal</td><td>Depende do que o fornecedor oferece.</td><td>Cupom ou nota emitidos direto do PDV, com integração à prefeitura.</td></tr></table></div>
<h2>Empresas atendidas</h2>{logos()}<p><a href="/projetos/">Ver projetos e clientes</a></p>
{backlinks()}
<h2>Avaliações no Google</h2><blockquote>Parabéns pelo trabalho, desta vez foi apenas o site da Supercon, em breve fará outros serviços, um ótimo parceiro!<cite>Supercon Construtora</cite></blockquote><blockquote>Excelente profissional, sempre demonstra competência, responsabilidade e dedicação em tudo o que faz.<cite>Lucas N.</cite></blockquote>
<h2>Pagamento por permuta</h2><p>Se a empresa não tem caixa agora, posso receber em produtos ou serviços. <a href="/permuta/">Veja como funciona a permuta</a>.</p>{cta("Falar com o Felipe")}''',prio="1.0")

# SERVIÇOS HUB
page("/servicos/","Serviços de Tecnologia para Empresas – Balneário Camboriú","Sites, sistemas e ERP sob medida, PDV, automações, SEO local e suporte de TI para empresas de Balneário Camboriú – SC e de todo o Brasil.","Serviços de tecnologia para empresas",
 f'<p class="lead">Seis serviços, cada um com a sua página. Escolha o que você precisa.</p><ul class="g">{cards}</ul>{cta()}',[("Serviços","/servicos/")],prio="0.9")
for s in SERV:
    slug,nome,t,d,h,intro,itens,fs=s
    svc={"@context":"https://schema.org","@type":"Service","name":nome,"description":d,"provider":{"@id":SITE+"/#negocio"},"areaServed":["Balneário Camboriú","Brasil"],"serviceType":nome}
    outros="".join(f'<li><a href="/servicos/{o[0]}/">{o[1]}</a></li>' for o in SERV if o[0]!=slug)
    page(f"/servicos/{slug}/",t,d,h,f'<p class="lead">{intro}</p><h2>O que está incluído</h2><ul>{"".join(f"<li>{i}</li>" for i in itens)}</ul>'
     f'<h2>Como funciona</h2><ol><li>Você conta o que precisa pelo WhatsApp.</li><li>Eu analiso o caso e envio orçamento e prazo por escrito.</li><li>Desenvolvo e mostro o andamento.</li><li>Entrego, treino quem vai usar e continuo no suporte.</li></ol>{cta()}{faq(fs)}<h2>Outros serviços</h2><ul>{outros}</ul>',
     [("Serviços","/servicos/"),(nome,f"/servicos/{slug}/")],svc,"0.8")

page("/sobre/","Sobre Felipe Goulart – Desenvolvedor em Balneário Camboriú","Felipe Goulart, desenvolvedor de software em Balneário Camboriú – SC. Tecnólogo em Gestão Financeira, estuda Engenharia de Software e atua há cerca de 4 anos.","Sobre Felipe Goulart",
 FELIPE_SP+'<p class="lead">Tenho 24 anos, nasci em Pato Branco (PR) e moro em Balneário Camboriú – SC. Trabalho há cerca de 4 anos com desenvolvimento de software e serviços digitais.</p><p>Sou tecnólogo em Gestão Financeira e curso Engenharia de Software. A formação financeira ajuda a entender o processo da empresa antes de escrever o sistema.</p><h2>Tecnologias que uso</h2><p>GitHub, Supabase, Cursor e Google Business Profile, entre outras ferramentas de desenvolvimento, banco de dados e marketing local.</p>'+cta("Falar com o Felipe"),[("Sobre","/sobre/")],prio="0.6")

page("/projetos/","Projetos e Clientes – Felipe Goulart","Projetos de Felipe Goulart: sistemas de transporte, PDV, CRM, plataforma de automação e sites de hotel e varejo em Santa Catarina.","Projetos e clientes atendidos",
 f'''<p class="lead">Sistemas e sites que desenvolvi, com o endereço de cada um.</p>
<div class="tb"><table><tr><th>Projeto</th><th>Tipo</th><th>Endereço</th></tr>
<tr><td>Painel E-Transporte.pro</td><td>Sistema de reservas, motoristas e clientes</td><td>business.transporteexecutivo.com</td></tr>
<tr><td>Transporte Executivo</td><td>Site</td><td><a href="https://www.transporteexecutivo.com" rel="noopener">www.transporteexecutivo.com</a></td></tr>
<tr><td>PDV SmartPlanet</td><td>PDV, estoque, caixa e financeiro</td><td>pdv.lojadeeletronicossaojose.com.br</td></tr>
<tr><td>SmartPlanet – a Boutique do Celular</td><td>Site de loja em São José – SC</td><td><a href="https://www.lojadeeletronicossaojose.com.br" rel="noopener">www.lojadeeletronicossaojose.com.br</a></td></tr>
<tr><td>Hotel Blumenau</td><td>Site de hotel com reserva online, Balneário Camboriú – SC</td><td><a href="https://www.hotelblumenau.com.br" rel="noopener">www.hotelblumenau.com.br</a></td></tr>
<tr><td>API-Construtor.PRÓ</td><td>Plataforma de fluxos de automação de mensagens</td><td><a href="https://www.api-construtor.pro" rel="noopener">www.api-construtor.pro</a></td></tr>
<tr><td>FirestepCRM</td><td>CRM com agenda, clientes e financeiro</td><td>crm.firestep.cloud</td></tr>
<tr><td>Firestep – Sites e CRM</td><td>Site com modelos prontos e CRM</td><td><a href="https://www.firestep.cloud" rel="noopener">www.firestep.cloud</a></td></tr></table></div>
<h2>Clientes</h2>{logos()}{backlinks()}{cta()}''',[("Projetos","/projetos/")],prio="0.7")

page("/permuta/","Permuta: Site e Sistema em Troca de Produtos ou Serviços","Faço site, sistema, automação e suporte de TI e recebo em produtos ou serviços da sua empresa. Permuta com empresas de todo o Brasil.","Permuta: tecnologia em troca de produtos ou serviços",
 f'<p class="lead">Se a empresa não tem caixa agora, posso receber em produtos, serviços ou mercadoria para revenda, em vez de dinheiro.</p><h2>O que eu entrego</h2><ul><li>Site ou loja virtual</li><li>Sistema, ERP ou PDV</li><li>Automação e WhatsApp</li><li>Suporte de TI</li><li>Perfil no Google Maps e SEO local</li><li>Infraestrutura e redes</li></ul><h2>O que você pode oferecer</h2><ul><li>Produtos do estoque</li><li>Serviços da empresa</li><li>Mercadoria para revenda</li><li>Equipamentos</li><li>Veículos ou locação</li></ul><p>Conte o que a empresa tem e o valor aproximado. Se a conta não fechar, ajustamos ou deixamos para outro momento.</p><p><a class="btn" href="{wa("Olá, Felipe! Quero propor uma permuta. Minha empresa:")}">Propor permuta no WhatsApp</a></p>',[("Permuta","/permuta/")],prio="0.5")

page("/contato/","Contato – Felipe Goulart – Balneário Camboriú – SC","Fale com Felipe Goulart pelo WhatsApp (47) 99123-7643 ou e-mail. Orçamento de sites, sistemas, ERP, PDV e suporte de TI. Balneário Camboriú – SC.","Contato",
 f'<p class="lead">Orçamentos e dúvidas sobre sites, sistemas, PDV, automações e suporte de TI.</p><div class="tb"><table><tr><th>WhatsApp</th><td><a href="{WA}">{FONE}</a></td></tr><tr><th>E-mail</th><td><a href="mailto:{MAIL}">{MAIL}</a></td></tr><tr><th>Local</th><td>Balneário Camboriú – SC</td></tr><tr><th>Atendimento</th><td>Todo o Brasil</td></tr></table></div>{cta("Chamar")}',[("Contato","/contato/")],prio="0.8")

open(OUT+"/404.html","w",encoding="utf-8").write('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Página não encontrada – Felipe Goulart</title><link rel="stylesheet" href="/style.css"></head><body><main class="w"><h1>Página não encontrada</h1><p><a href="/">Voltar para o início</a> ou ver os <a href="/servicos/">serviços</a>.</p></main></body></html>')
open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>\n" for u,p in sitemap)+"</urlset>")
open(OUT+"/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
from urllib.parse import urlparse
HOST=urlparse(SITE).netloc
open(OUT+"/vercel.json","w").write(json.dumps({"redirects":[{"source":"/(.*)","has":[{"type":"host","value":"www."+HOST}],"destination":SITE+"/$1","permanent":True}] if not HOST.startswith("www.") else [],"cleanUrls":True,"trailingSlash":True,"headers":[
 {"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"X-Frame-Options","value":"SAMEORIGIN"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"},{"key":"Permissions-Policy","value":"camera=(), microphone=(), geolocation=()"}]},
 {"source":"/img/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
 {"source":"/style.css","headers":[{"key":"Cache-Control","value":"public, max-age=86400"}]}]},indent=2))
print(len(sitemap),"páginas")
