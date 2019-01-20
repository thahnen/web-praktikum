<!-- Navigationsleiste -->
<ul>
@var entry;@
@var loop;@
@for loop = 0; loop < context.length; loop++@
	@entry = context[loop];@
	<li>
   		<a href="##" data-action="#entry[0]#">#entry[1]#</a>
   	</li>
@endfor@
</ul>
