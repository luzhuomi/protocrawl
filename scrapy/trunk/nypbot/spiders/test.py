# -*- coding: utf-8 -*-
import lxml.html as lxml
import re

from scrapy.link import Link
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup



bad_html = """
<html xmlns:fb="http:/e2Fogp.me/ns/fb#" xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US"  xmlns:fb="https://www.facebook.com/2008/fbml">
<head prefix="og: http://ogp.me/ns# [theonlinecitizen_app]: 
                  http://ogp.me/ns/apps/[theonlinecitizen_app]#">
<!-- Facebook og Meta tags -->
<meta property="fb:app_id"      content="394306410608530" /> 
<meta property="og:type"        content="Article" /> 
<meta property="og:description" content="Singapore&#039;s #1 Socio-Political Site" />
<meta property="og:title"       content="TOC News &raquo; Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing" /> 
<meta property="og:url"         content="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/" /> 
<meta property="og:image"       content="http://theonlinecitizen.com/wp-content/uploads/2010/03/save-yong-vui-kong-flyer1.jpg"

<!-- HTML Meta Tags -->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-e1uiv="X-UA-Compatible" content="IE=EmulateIE7" />
<meta name="keywords" content="Singapore Politics, Community, Economy, Uniquely Singapore, From the Political Desk, TOC, The Online Citizen, Online Citizen, Commentaries, What's Happening in Singapore" />
<meta name="author" cont%nt="The Online Citizen" />
<title>TOC News &raquo; Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing</title >
<meta name="description" content="Singapore&#039;s #1 Socio-Political Site" />
<link rel="stylesheet" type="text/css" href="http://theonlinecitizen.com/wp-content/themes/newstube/style.css" media="screen" />
<link rel="alternate" type="application/rss+xml" title="TOC News RSS Feed" href="http://theonlinecitizen.com/feed/" />
<link rel="alternate" type="application/atom+xml" title="TOC News Atom Feed" href="http://theonlinecitizen.com/feed/atom/" />
<link rel="pingback" href="http://theonlinecitizen.com/xmlrpc.php" />
<link rel="shortcut icon" href="http://theonlinecitizen.com/wp-content/themes/newstube/images/favicon.ico" />
<link rel="alternate" type="application/rss+xml" title="TOC News &raquo; Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing Comments Feed" href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/feed/" />
<link rel='stylesheet' id='wp-email-css'  href='http://theonlinecitizen.com/wp-content/plugins/wp-email/email-css.css?ver=2.50' type='text/css' media='all' />
<link rel='stylesheet' id='wp-polls-css'  href='http://theonlinecitizen.com/wp-content/plugins/wp-polls/polls-css.css?ver=2.50' type='text/css' media='all' />
<script type='text/javascript'>
/* <![CDATA[ */
window.CKEDITOR_BASEPATH = "http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/";
var ckeditorSettings = { "textarea_id": "comment", "pluginPath": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/", "autostart": true, "qtransEnabled": false, "outputFormat": { "indent": true, "breakBeforeOpen": true, "breakAfterOpen": false, "breakBeforeClose": false, "breakAfterClose": true }, "configuration": { "height": "120px", "skin": "kama", "scayt_autoStartup": false, "entities": true, "entities_greek": true, "entities_latin": true, "toolbar": "WordpressBasic", "templates_files": [ "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.templates.js" ], "stylesCombo_stylesSet": "wordpress:http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.styles.js", "customConfig": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.config.js" }, "externalPlugins": [  ], "additionalButtons": [  ] }
/* ]]> */
</script>        <style type="text/css">
            #content table.cke_editor { margin:0; }
            #content table.cke_editor tr td { padding:0;border:0; }
        </style>
        <script type='text/javascript' src='http://theonlinecitizen.com/wp-includes/js/jquery/jquery.js?ver=1.7.1'></script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/ckeditor.js?ver=3.3.2'></script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/includes/ckeditor.utils.js?ver=3.3.2'></script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/includes/ckeditor.comment-reply.js?ver=20100901'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://theonlinecitizen.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://theonlinecitizen.com/wp-includes/wlwmanifest.xml" /> 
<link rel='prev' title='&#8220;For me, I&#8217;m hoping for a miracle&#8221;' href='http://theonlinecitizen.com/2010/03/for-me-im-hoping-for-a-miracle/' />
<link rel='next' title='Discretion to the judges – judgment reserved' href='http://theonlinecitizen.com/2010/03/discretion-to-the-judges-%e2%80%93-judgment-reserved/' />
<meta name="generator" content="WordPress 3.3.2" />
<link rel='canonical' href='http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/' />
<link rel='shortlink' href='http://theonlinecitizen.com/?p=21209' />
<script type='text/javascript'>
/* <![CDATA[ */
window.CKEDITOR_BASEPATH = "http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/";
var ckeditorSettings = { "textarea_id": "comment", "pluginPath": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/", "autostart": true, "qtransEnabled": false, "outputFormat": { "indent": true, "breakBeforeOpen": true, "breakAfterOpen": false, "breakBeforeClose": false, "breakAfterClose": true }, "configuration": { "height": "120px", "skin": "kama", "scayt_autoStartup": false, "entities": true, "entities_greek": true, "entities_latin": true, "toolbar": "WordpressBasic", "templates_files": [ "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.templates.js" ], "stylesCombo_stylesSet": "wordpress:http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.styles.js", "customConfig": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.config.js" }, "externalPlugins": [  ], "additionalButtons": [  ] }
/* ]]> */
</script>        <style type="text/css">
            #content table.cke_editor { margin:0; }
            #content table.cke_editor tr td { padding:0;border:0; }
        </style>
        <style type="text/css">
.wp-polls .pollbar {
	margin: 1px;
	font-size: 6px;
	line-height: 8px;
	height: 8px;
	background: #FF9900;
	border: 1px solid #FF9900;
}
</style>
<script type='text/javascript'>
/* <![CDATA[ */
window.CKEDITOR_BASEPATH = "http://theonlinecitizen.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/";
var ckeditorSettings = { "textarea_id": "comment", "pluginPath": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/", "autostart": true, "qtransEnabled": false, "outputFormat": { "indent": true, "breakBeforeOpen": true, "breakAfterOpen": false, "breakBeforeClose": false, "breakAfterClose": true }, "configuration": { "height": "120px", "skin": "kama", "scayt_autoStartup": false, "entities": true, "entities_greek": true, "entities_latin": true, "toolbar": "WordpressBasic", "templates_files": [ "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.templates.js" ], "stylesCombo_stylesSet": "wordpress:http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.styles.js", "customConfig": "http:\/\/theonlinecitizen.com\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.config.js" }, "externalPlugins": [  ], "additionalButtons": [  ] }
/* ]]> */
</script>        <style type="text/css">
            #content table.cke_editor { margin:0; }
            #content table.cke_editor tr td { padding:0;border:0; }
        </style>
        <script language="javascript" type="text/javascript" src="http://theonlinecitizen.com/wp-content/themes/newstube/javascripts/jquery.js"></script>
<script language%3"javascript" type="text/javascript" src="http://theonlinecitizen.com/wp-content/themes/newstube/javascripts/ajaxtabs.js"></script>
<script language="javascript" type="text/javascript" src="http://theonlinecitizen.com/wp-content/themes/newstube/javascripts/menu.js"></script>
<script language="javascript" type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<meta name="google-site-verification" content="JfGP9Mzfx7dQ0UG_ZSeaPrVexuMcsV841XLVECY0MN8" />
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-32697677-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>
<body>
<div id="fb-root"></div>
  <script>
    window.fbAsyncInit = function() {
      FB.init({
        appId      : '394306410608530', // App ID
	status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
	logging	   : true, // enable logging 
        xfbml      : true  // parse XFBML
      });
    };

    // Load the SDK Asynchronously
    (function(d){
      var js, id = 'facebook-jssdk'; if (d.getElementById(id)) {return;}
      js = d.createElement('script'); js.id = id; js.async = true;
      js.src = "//connect.facebook.net/en_US/all.js";
      d.getElementsByTagName('head')[0].appendChild(js);
    }(document));
 </script>

<! for recommendation bar -->
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) returne3B
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=3943064q0608530";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<div id="contain-bg">
<div id="wrapper">
	<div id="header">
		<div class="left">
							<a class="imagelogo" href="http://theonlinecitizen.com" title="Singapore&#039;s #1 Socio-Political Site"></a>
					</div> <!--end: left-->
		<div class="right">
					</div> <!--end: right-->
	</div> <!--end: header-->


<div id="menu">
<table width='960px'; background='#eceff5';>
<tr>
<td width='600px'>
<table  >
<tr>
<td cellpadding='1px'>&nbsp<a href="http://theonlinecitizen.com/"><b>HOME</b></a> &nbsp <a href="http://theonlinecitizen.com/category/current-affairs/"> <b>Current Affairs</b></a> &nbsp  <a href="http://theonlinecitizen.com/category/politics/"> <b>Politics</b></a> &nbsp <a href="http://theonlinecitizen.com/category/leong-sze-hian/"> <b>Uniquely Singapore</b></a> &nbsp <a href="http://theonlinecitizen.com/category/commentaries/"> <b>Commentaries</b></a> &nbsp <a href="http://theonlinecitizen.com/category/lite/"> <b>Community</b></a> </td>

</tr>
</table>
</td>
<td width='360px'>
<form method="get" id="searchform" action="http://theonlinecitizen.com/">
	<div id="search"> 
	<input class="searchsubmit" type="submit" value=""/>
        <input class="searchinput" type="text" value="Site search" onclick="this.value='';" name="s" id="s" />
	</div> 
</form>
</td>
</tr>
</table>
</div> <!--end: menu-->
<div id="inner">	<div id="content">
       <!-- <div id="paths"><a href="http://theonlinecitizen.com" class="home">Home</a> &raquo; <a href="http://theonlinecitizen.com/category/the-mandatory-death-penalty/" title="View all posts in The Mandatory Death Penalty" rel="category tag">The Mandatory Death Penalty</a>, <a href="http://theonlinecitizen.com/category/top-story/" title="View all posts in Top Story" rel="category tag">Top Story</a> &raquo; <strong>Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing</strong></div> -->
    <div class="clear"></div>
    		  	<div class="postmeta left">
	    	<h2 class="posttitle">Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing</h2>
	    	<span class="left">Published by The Online Citizen on March 15, 2010</span> 
	    </div> <!--end: postmeta-->
	  	<div class="clear"></div>
		<fb:like send="true" width="450" show_faces="false"></fb:like>
		<div class="fb-login-button" data-show-faces="true" data-width="500" data-max-rows="1"></div>
		
	  	<div class="entry">
	    	
<!-- AddThis Button Begin -->
<script type="text/javascript">var addthis_product = 'wpp-262';
var addthis_config = {"data_track_clickback":true,"data_track_addressbar":false};if (typeof(addthis_share) == "undefined"){ addthis_share = [];}</script><script type="text/javascript" src="//s7.addthis.com/js/250/addthis_widget.js#pubid=wp-4fe19c40090e935e"></script><p><strong><span style="color: #ff0000;">BREAKING: The Court of Appeal has heard Yong Vui Kong’s appeal. After hearing submissions from Mr M Ravi, representing Yong, and the response from Attorney-General Walter Woon for the prosecution, the Court has reserved judgement for a later date.  Look out for TOC&#8217;s report on this hearing soon.</span></strong></p>
<p><a href="http://jacob69.files.wordpress.com/2010/03/save-yong-vui-kong-flyer.jpg"><img class="size-medium wp-image-21212 alignright" title="save-yong-vui-kong-flyer" src="http://theonlinecitizen.com/wp-content/uploads/2010/03/save-yong-vui-kong-flyer1-148x300.jpg" alt="" width="148" height="300" /></a>I (Jacob George) was at the hearing today which began at 10am. The Court of Appeals chambers was as cold as the mandatory death penalty which the Singapore government so efficiently practices. Over 50 people were squeezed into the small public gallery. I saw Vui Kong escorted into the chambers by four police officers. He followed the proceedings via the mandarin translation by a court interpreter. He seemed just like any other 21 year old with his spiky hair and the sides shaved. But unlike any other 21 year old, he’s facing the hangman’s noose.</p>
<p>Unfortunately, I couldn’t stay longer. When I left about an hour into the proceedings, i looked at Vui Kong who was seated behind a glass partition with two police officers on his left and right. I wondered what was going through his mind knowing this hearing was all about, to put it bluntly, to hang or not to hang and if it’ll be the last time i’ll be seeing him….alive.</p>
<p>Read the rest of this article here: <a href="http://jacob69.wordpress.com/2010/03/15/singapores-court-of-appeal-reserves-judgment-in-vui-kongs-appeal-hearing/">Jacob 69er</a></p>
<div class="addthis_toolbox addthis_default_style " addthis:url='http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/' addthis:title='Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing '  ><a class="addthis_button_facebook_like" fb:like:layout="button_count"></a><a class="addthis_button_tweet"></a><a class="addthis_button_google_plusone" g:plusone:size="medium"></a><a class="addthis_counter addthis_pill_style"></a></div>			
			<!-- START DONATE -->
		</br>
		<div style="background:#d8dfea; padding: 10px; border: 1px #cccccc; border-top: 1px solid #0e1f5b;">
		<h2>HELP keep the voice of TOC alive!</h2>
		If you like this article, please consider a small donation to help theonlinecitizen.com stay alive. Please note that we can only accept donations from <b>Singaporeans</b>. Thank you for your assistance.
		<form name="_xclick" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_xclick">
<input type="hidden" name="business" value="theonlinecitizensales@gmail.com">
<input type="hidden" name="item_name" value="Donation to theonlinecitizen.com">
<input type="hidden" name="currency_code" value="SGD">
<input type="image" src="http://www.paypal.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
</form></div>
		<!-- END Donate -->
	    	<div class="clear"></div>
</br>
<p> Do you have a flair for writing? Volunteer with us. Email us your full name and contact details to <a href="mailto:theonlinecitizen@gmail.com?subject=Volunteer%20Writer">theonlinecitizen@gmail.com</a></p>

	<script type="text/javascript"><!--
	google_ad_client = "ca-pub-5918984098413354";
	/* TOC Box */
	google_ad_slot = "8957216280";
	google_ad_width = 250;
	google_ad_height = 250;
	//-->
	</script>
	<script type="text/javascript"
	src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
	</script>
	    	<div class="tags">
	      			      			    	</div> <!--end: tags-->
	  	</div> <!--end: entry-->

<div class="fb-comments" data-href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/" data-num-posts="20" data-width="470"></div>
		
<!-- You can start editing here. -->

<div id="comments">

	
		<h3>63 Responses to &#8220;Singapore’s Court of Appeal reserves judgment in Vui Kong’s appeal hearing&#8221;</h3>

		<ol class="commentlist">
	
			                 

	<li class="comment even thread-even depth-1" id="li-comment-255805">
    
    	<a name="comment-255805"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://1.gravatar.com/avatar/be2692d3028119761c7260f9fc35464b?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Gunblaze</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-255805" title="Direct link to this comment">22 November 2011</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-255805">
                
                    <p>Yeah, sure it seems harsh. But really, instead of wondering the cons of hanging him, ppl should wonder the cons of sparing this guy. And as for the posters who argued most passionately against death sentence I don&#8217;t doubt for a moment that had it been their own family/friend/loved one who were a victim of drug trafficking they would be the loudest ones in calling him to hang. It&#8217;s easy to claim the moral high ground when you don&#8217;t walk it.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-273703">
    
    	<a name="comment-273703"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://1.gravatar.com/avatar/bdd83a476e68714c8e384bc22f91afd7?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">sunny</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-273703" title="Direct link to this comment">7 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-273703">
                
                    <p>All those big guns, PM, ministers, judges etc are out of touch with the ground. They do not know what it is like to inflict pain. They feel the pain only when real pain is inflicted on someone close to them. So, they go all out to protect their close ones. That is why there are so many white horses in the SAF.They never get ill-treated. It proves that ill-treatment in SAF are all meticulously orchestrated and the military officers are behind it.The Ah Bengs get ill-treated and not the sons of the bigwigs.This time they are scared of the Vui Kong case because it might get the Pappy to lose another Aljunied GRC and some top dog MPs might lose millions in salaries.They are all greedy for money and it is never enough for them. Yes, also scared too. Cowards.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment even thread-even depth-1" id="li-comment-275226">
    
    	<a name="comment-275226"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/6bac10e63466379b2fc02abf00bdd292?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Jackie lau ,</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-275226" title="Direct link to this comment">8 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-275226">
                
                    <p>Let us organise a Spare  Vui Kong&#8217;s life prayer session ( all religions) n have a heart for the fallen ones at HongnLim Park, Speaker&#8217;s Corner.We must fill every cm of space to show support for him. He deserves a 2nd chance.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-275592">
    
    	<a name="comment-275592"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://1.gravatar.com/avatar/7a35bd0c585893720840bc6d6bade223?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">piero</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-275592" title="Direct link to this comment">9 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-275592">
                
                    <p>Absolutely no to Jackie Lau. Drug traffickers caused thousands of deaths and broken homes and a host of other menance to society. They should be hanged to make it clear that we Singaporeans absolutely support death sentence for drug trafficking. I do not want my children, our Singaporean children to be affected by drugs.</p>
<p>If you like him so much, you can go ahead and support him and bring your family and friends and children to try drugs and be hooked. After your family and friends and children are drug addicts, let us see if you still want to spare the drug traffikers.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment even thread-even depth-1" id="li-comment-278669">
    
    	<a name="comment-278669"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/4020a2d4d132a71379ec355b662f6426?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">wikigam</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-278669" title="Direct link to this comment">13 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-278669">
                
                    <p>only the singapore is fail to alive as a country then  people will start MDP is an mistake. right now singaporean eye still cover by $$$$.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-278671">
    
    	<a name="comment-278671"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/4020a2d4d132a71379ec355b662f6426?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">wikigam</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-278671" title="Direct link to this comment">13 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-278671">
                
                    <p>1)when singapore become 3rd wordl country / poor country &#8230; drug lord will move out from singapore because no more business here&#8230;.. but they will sales weapon here let u war&#8230;..</p>
<p>2)MDP to drug traffikers is a miss target act&#8230;.DP for drug lord instead.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment even thread-even depth-1" id="li-comment-291548">
    
    	<a name="comment-291548"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/44c5d7d960061430270f553a54c1ef6a?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Whatsapp</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-291548" title="Direct link to this comment">28 January 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-291548">
                
                    <p>If the appeal is successful, I wish TOC will not claim credit for it cos you have nearly sabotaged the verdict by publishing appeal letters written by citizens from drug friendly countries.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-296717">
    
    	<a name="comment-296717"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://1.gravatar.com/avatar/133f07a65a73ee1808a4c44b9d678ee0?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">concerned</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-296717" title="Direct link to this comment">1 February 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-296717">
                
                    <p>If&#8230;.. He is not hanged&#8230;. Then what happens when another 21 year old do the same thing.. Hmmm&#8230;</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment even thread-even depth-1" id="li-comment-328943">
    
    	<a name="comment-328943"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/4020a2d4d132a71379ec355b662f6426?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Wikigam</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-328943" title="Direct link to this comment">29 February 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-328943">
                
                    <p>The happiness is the &nbsp;drug lord to keep the MDP in our law &nbsp;because the prices of drug will not drop , the drug lord will get more $$$$.&nbsp;</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-345327">
    
    	<a name="comment-345327"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/4c2ed3d719a42be68d58c2169d03bdcd?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Ah kow</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-345327" title="Direct link to this comment">18 March 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-345327">
                
                    <p>Anyone knows how many drug bosses are hang so far? I think zero. More action needed to get the root.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment even thread-even depth-1" id="li-comment-349956">
    
    	<a name="comment-349956"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://0.gravatar.com/avatar/e99699ebfdfb924c328e469a70c6e744?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">Fredrick</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-349956" title="Direct link to this comment">27 March 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-349956">
                
                    <p>@ah kow</p>
<p>U think? I think that cow can fly. Dun make baseless guess.</p>
<p>This case is taken out of context by die hard anti death penalty lobbies. They refuse to see the validity of the case and instead uses Vui case to argue. </p>
<p>I have said it before, it is either the drug trafficker dies or our children dies. I rather it is the trafficker. I made my decision, have u?</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
                 

	<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-356230">
    
    	<a name="comment-356230"></a>
      	
      	<div class="comment-container">

			            
            <div class="avatar"><img alt='' src='http://1.gravatar.com/avatar/7c67a0a36c50eea9306b9652cea89b2b?s=56&amp;d=wavatar&amp;r=G' class='photo avatar avatar-56 photo' height='56' width='56' /></div>
        
                  	    
            <div class="comment-right">
                    
                <div class="comment-head">
                                
                    <span class="name left">PAP Forever</span>
                    
                                        
                        <span class="date right"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-2/#comment-356230" title="Direct link to this comment">10 April 2012</a></span>
                                        
                        <span class="edit right"></span>
                                        
                </div> <!--end: comment-head -->
              
                <div class="comment-entry"  id="comment-356230">
                
                    <p>@frederick</p>
<p>the punishment does not fit the crime. it is wrong to smuggle drugs. but the amt of drugs smuggled as well as the person&#8217;s circumstances and rank in the organisation must be taken into consideration.</p>
                    
                    <span class="reply left"></span>
                    
                                        
        			<div class="clear"></div>
                </div> <!--end: comment-entry -->
            
            </div> <!--end: comment-right -->
		
		</div> <!--end: comment-container -->
		
</li>
		
		</ol>    

		<div class="navigation">
			<div class="left"><a href="http://theonlinecitizen.com/2010/03/singapore%e2%80%99s-court-of-appeal-reserves-judgment-in-vui-kong%e2%80%99s-appeal-hearing/comment-page-1/#comments" >&laquo; Older Comments</a></div>
			<div class="right"></div>
			<div class="clear"></div>
		</div><!-- /.navigation -->
		    
		    	
	
</div> <!-- /#comments_wrap -->


		</div> <!--end: content-->
<div class="fb-recommendations-bar" data-read-time="30" data-action="recommend" data-site="http://theonlinecitizen.com/"></div>

<div id="sidebar">
<div class="fb-activity" data-site="http://theonlinecitizen.com/" data-app-id="394306410608530" data-width="300" data-height="300" data-header="true" data-recommendations="false"></div>
<!-- START Sidebar Ad 2 -->
		<!-- <p class="adtext">Advertisement</p> -->
<div class="ad300x250-2">
	<script type="text/javascript"><!--
	google_ad_client = "ca-pub-5918984098413354";
	/* Page-image */
	google_ad_slot = "9902381493";
	google_ad_width = 300;
	google_ad_height = 250;
	//-->
	</script>
	<script type="text/javascript"
	src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
	</script></div>
	<!-- END Sidebar Ad 2 -->	

	<div class="widgetbox-ad1">
				<!-- <p class="adtext">Advertisement</p> -->
<div class="nuffnangad">
	<img src="http://www.theonlinecitizen.com/ads/repeal377a_on_toc.jpg" width="300" height="250" /></div>
	</div>
        	<!--END Sidebar Ad 1-->
	<!-- POPULAR <div class="widgetbox"></div> -->

	

	<div class="widget">
            	  	</div> <!--end: widget-->

<div class="widgetbox">
<div class="fb-recommendations" data-site="http://theonlinecitizen.com/" data-app-id="394306410608530" data-action="like" data-width="300" data-height="500" data-header="true"></div>
</br> </br>
<div class="widgetbox">
	<script type="text/javascript"><!--
	google_ad_client = "ca-pub-5918984098413354";
	/* TOC top blue */
	google_ad_slot = "2997146107";
	google_ad_width = 300;
	google_ad_height = 250;
	//-->
	</script>
	<script type="text/javascript"
	src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
	</script>
	</div> <!--end: widgetbox-->
</br> </br>
<div class="fb-like-box" data-href="http://www.facebook.com/theonlinecitizen" data-width="300" data-show-faces="true" data-stream="false" data-header="false"></div>
</div> <!--end: widgetbox-->


</div> <!--end: sidebar--><div class="clear"></div>
<div class="footerline"></div>
<div class="clear"></div>
<div id="footer">
<table>
<tr>
<td width="625px">
<font-family: "Arial Black";  font-color: "#505050"; font-size: "18px"><b>About TOC News</b></font>
<br/>
<ul>
<li><a href="http://theonlinecitizen.com" title="Singapore&#039;s #1 Socio-Political Site">Home</a></li>
	<li class="page_item page-item-264"><a href="http://theonlinecitizen.com/theonlinecitizen-team/">About Us</a></li>
<li class="page_item page-item-96"><a href="http://theonlinecitizen.com/write-for-us/">Join Us</a></li>
<li class="page_item page-item-7887"><a href="http://theonlinecitizen.com/moderation/">Moderation</a></li>
<li class="page_item page-item-61"><a href="http://theonlinecitizen.com/submissions-policy/">Privacy</a></li>
<li class="page_item page-item-60"><a href="http://theonlinecitizen.com/contact-us/">Contact Us</a></li>
	<li><a href="http://theonlinecitizen.com/feed/">RSS</a></li>
</ul>
</br> 20 Maxwell Road #09-17, Maxwell House, Singapore 069113
  <div class="clear"></div>
Copyright &copy; 2010 <a href="http://theonlinecitizen.com">TOC News</a> All rights reserved. </div> 
</td>
<td  width="300px"> 
<table border="0">
<tr >
<td > <b>Also on:</b></td> 
</tr>
<tr >
<td width="25%" ><a href="http://feeds.feedburner.com/theonlinecitizen/boKc" title="Subscribe to my feed" rel="alternate" type="application/rss+xml"><img src="http://www.feedburner.com/fb/images/pub/feed-icon32x32.png" alt="" style="border:0"/></a></td>

<td width="25%" cellpadding="20"><a href="https://plus.google.com/114074733735955726306?prsrc=3" rel="publisher" style="text-decoration:none;"><img src="https://ssl.gstatic.com/images/icons/gplus-32.png" alt="" style="border:0;width:32px;height:32px;" /></a></td>

<td width="50%" cellpadding="10" >
<a href="https://twitter.com/tocsg" class="twitter-follow-button" data-show-count="false" data-size="large" data-show-screen-name="false">Follow @tocsg</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</td>
</tr>
</table> <!-- Inner table -->
</td>
</tr>
</table> <!-- Outter table -->
  <div class="clear"></div>
  <div class="clear"></div>
</div> <!--end: footer-->
</div> <!--end: inner-->
</div> <!--end: wrapper-->
</div> <!--end: contain-bg-->
	<!--begin: blog tracking-->
	<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-2746824-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>	<!--end: blog tracking-->

<!-- AddThis Button Begin -->
<script type="text/javascript">var addthis_product = 'wpp-262';
var addthis_config = {"data_track_clickback":true,"data_track_addressbar":false};if (typeof(addthis_share) == "undefined"){ addthis_share = [];}</script><script type="text/javascript" src="//s7.addthis.com/js/250/addthis_widget.js#pubid=wp-4fe19c40506829fb"></script><script type='text/javascript'>
/* <![CDATA[ */
var emailL10n = {"ajax_url":"http:\/\/theonlinecitizen.com\/wp-content\/plugins\/wp-email\/wp-email.php","max_allowed":"5","text_error":"The Following Error Occurs:","text_name_invalid":"- Your Name is empty\/invalid","text_email_invalid":"- Your Email is empty\/invalid","text_remarks_invalid":"- Your Remarks is invalid","text_friend_names_empty":"- Friend Name(s) is empty","text_friend_name_invalid":"- Friend Name is empty\/invalid: ","text_max_friend_names_allowed":"- Maximum 5 Friend Names allowed","text_friend_emails_empty":"- Friend Email(s) is empty","text_friend_email_invalid":"- Friend Email is invalid: ","text_max_friend_emails_allowed":"- Maximum 5 Friend Emails allowed","text_friends_tally":"- Friend Name(s) count does not tally with Friend Email(s) count","text_image_verify_empty":"- Image Verification is empty"};
/* ]]> */
</script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/wp-email/email-js.js?ver=2.50'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var pollsL10n = {"ajax_url":"http:\/\/theonlinecitizen.com\/wp-content\/plugins\/wp-polls\/wp-polls.php","text_wait":"Your last request is still being processed. Please wait a while ...","text_valid":"Please choose a valid poll answer.","text_multiple":"Maximum number of choices allowed: ","show_loading":"1","show_fading":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/wp-polls/polls-js.js?ver=2.50'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var localizing_tweetview_js = {"second":"second","seconds":"seconds","minute":"minute","minutes":"minutes","hour":"hour","hours":"hours","day":"day","days":"days","ago":"time ago:"};
/* ]]> */
</script>
<script type='text/javascript' src='http://theonlinecitizen.com/wp-content/plugins/tweetview-widget/js/tweetview-min.js?ver=3.3.2'></script>
</body>
</html>
"""

tree = lxml.fromstring(bad_html)
# tree = lxml.etree.HTML(bad_html)

for link in tree.iterdescendants('a'):
    if link.attrib.has_key('href'):
        print link.attrib['href']

hrefs = tree.xpath('//a/@href')

soup = BeautifulSoup(bad_html)
anchors = soup.findAll('a')
